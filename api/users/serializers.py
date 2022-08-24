from rest_framework import serializers

from api.users.models import User, Appointment

class ListUserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "first_name", 
            "last_name",
        ]

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username", 
            "password", 
            "first_name", 
            "last_name",            
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    """
    User Serliazer used for update(), partial_update() and retrieve()
    """
    appointments = AppointmentSerializer(many=True, required=False)
    
    class Meta:
        model = User
        fields = [
            "id", 
            "username", 
            "first_name", 
            "last_name",
            "phone_number",
            "medical_history",
            "info",
            "email",
            "pdf",
            "picture",
            "appointments",
        ]
    
class ChangePasswordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "password",
        ]    


