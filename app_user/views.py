from django.contrib.auth import authenticate, get_user_model

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from app_user.serializers import RegisterSerializer, LoginSerializer

UserModel = get_user_model()


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserModel.objects.all()


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            response = {
                "token": token.key,
                "username": user.username,
                "phone_number": user.phone_number
            }
            return Response(response, status=status.HTTP_200_OK)

        else:
            return Response({'message': 'Invalid credentials'}, status=401)
