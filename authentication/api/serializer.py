from authentication.models import UserModel
from django.db import models
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    
    password = models.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = "__all__"

    #TODO VALIDATIONS.

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)
    
    # ** unpacks the dictionary as validated data is a dictionary in in the create method.