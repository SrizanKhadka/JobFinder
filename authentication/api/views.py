from rest_framework.response import Response
from authentication.api.serializer import UserSerializer
from authentication.models import UserModel
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import permissions

class UserRegistrationAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [permissions.AllowAny]


class UserLoginAPIView(APIView):
    
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username,password=password)
        print(f"Logging in with username = {username} and password = {password}")

        if user:
            token, created = Token.objects.get_or_create()
            return Response({"token" : token.key, "created":created})
        else:
            return Response({"error": "Invalid credentials. Plese enter valid username and passwod"}, status=401)
            



        