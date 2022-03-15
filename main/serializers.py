from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Request
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password","first_name","last_name"]
    def create(self, validated_data):
        obj = User.objects.create(**validated_data)
        obj.set_password(validated_data["password"])
        obj.save()
        return obj
class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Profile
        fields=["user","phone","department","status"]
    
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Request
        fields=[
            "name",
            "description",
            "created_by",
            "last_modified",
            "timestamp",
            "status"
            ]
    
    