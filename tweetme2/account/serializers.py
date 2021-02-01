from django.db.models.fields import EmailField
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# User Serializer
#Pillamos el usuario
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
    def validate(self, data):
        # Comprobamos que el correo no exista
        if User.objects.filter(email=data["email"]) == []:
            raise serializers.ValidationError("Email registered before")
            
        if  len(data['password']) < 8 :
            raise serializers.ValidationError("Password must have at least 8 characters")
        return data
    