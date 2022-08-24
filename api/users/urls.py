from django.urls import path, include

from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'appointment', AppointmentViewSet)


urlpatterns = [    
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('', include(router.urls)),
]