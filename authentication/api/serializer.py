from authentication.models import UserModel
from rest_framework.response import Response
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = "__all__"

    def validate(self, data):
        username = data["username"]
        email = data["email"]

        print(f"USERNAME = {username}")

        if UserModel.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error":"A user with the email already exists!"})
        
        return data

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    # ** unpacks the dictionary as validated data is a dictionary in in the create method.
