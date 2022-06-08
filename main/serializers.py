from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Attachment, CostModel, Feedback, Profile, Request
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password","first_name","last_name"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        obj = User.objects.create(**validated_data)
        obj.set_password(validated_data["password"])
        obj.save()
        return obj
class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Profile
        fields=["id","user","phone","department","status"]
    

class CostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CostModel
        fields="__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields="__all__"

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attachment
        fields="__all__"
class RequestSerializer(serializers.ModelSerializer):
    cost_model=CostModelSerializer(many=True,required=False)
    attachments=AttachmentSerializer(many=True,required=False)
    class Meta:
        model=Request
        fields=["id",
            "name",
            "description",
            "created_by",
            "last_modified",
            "timestamp",
            "status",
            "attachments",
            "cost_model",
            "comment"
            ]
        
        read_only_fields=['cost_model']
        extra_kwargs = {"attachments": {"required": False, "allow_null": True},
        "comment": {"required": False, "allow_null": True},
        }
        