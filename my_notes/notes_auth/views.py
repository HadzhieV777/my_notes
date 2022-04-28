from django.contrib.auth import get_user_model
from rest_framework import generics as api_generic_views
from rest_framework import views as api_views
from rest_framework.authtoken import views as auth_views
from notes_auth.serializers import CreateUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

UserModel = get_user_model()


class RegisterView(api_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginView(auth_views.ObtainAuthToken):
    pass


class LogoutView(api_views.APIView):
    @staticmethod
    def __perform_logout(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({
            'message': 'Successfully logged out'
        })

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)
