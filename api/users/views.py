import jwt, datetime
import os

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import User
from .serializers import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

class LoginView(APIView):

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        # Create token and return token via cookies
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        # response.data = {"jwt": token}
        response.data = token
        return response


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"messsage": "success"}

        return response

class UserViewSet(ModelViewSet):
    """
    Multiple serializers DRF ModelViewSet to provide all default CRUD operations regarding User model
            
    Actions
    -------
    list(): 
    ["GET"] List all users profiles by username and name
    
    create():
    ["POST"] Regsiters a user profile with username and password

    update():
    ["PUT"] Edit/Update user profile
    
    retrieve():
    ["GET"] Return specific user users/<pk:int> full profile
    
    change_password():
    ["PATCH"] Change user profile login password
    """
    queryset = User.objects.all()
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    
    action_serializer_classes = {
        "list": ListUserSerailizer,
        "create": UserRegisterSerializer,
        "update": UserSerializer,
        "partial_update": UserSerializer,
        "retrieve": UserSerializer,
        "change_password": ChangePasswordSerializer,
        "metadata": UserSerializer,
     }
    
    def get_serializer_class(self):
        return self.action_serializer_classes[self.action]
    
    def update(self, request, *args, **kwargs):
        print(request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
        
    @action(detail=True, methods=['patch'])
    def change_password(self, request, pk=None):
        """
        Change user password. Password can be changed with the requirement for old password
        """
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password changed'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            

class AppointmentViewSet(ModelViewSet):
    """
    DRF ModelViewSet to provide all default CRUD operations regarding booking an appointment
    """
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    


    def create(self, request, *args, **kwargs):
        print(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
# class UserView(APIView):

#     def get(self, request):
#         token = request.COOKIES.get("jwt")

#         if not token:
#             raise AuthenticationFailed("Unauthenticated!")

#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed("Unauthenticated!")

#         user = User.objects.filter(id=payload["id"]).first()
#         serializer = UserSerializer(user)

#         return Response(serializer.data)
