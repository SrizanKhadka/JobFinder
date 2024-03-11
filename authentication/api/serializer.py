from authentication.models import UserModel
from rest_framework.response import Response
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = "__all__"

    def validate(self, data):
        if data["userCountry"]:
            return Response({"error": "User coutry is required!"})
        elif data["userAge"]:
            return Response({"error": "User Age is required!"})

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)

    # ** unpacks the dictionary as validated data is a dictionary in in the create method.
