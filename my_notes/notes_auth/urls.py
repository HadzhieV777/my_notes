from django.urls import path
from notes_auth.views import LoginView, LogoutView
from notes_auth.views import RegisterView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
    path('logout/', LogoutView.as_view(), name='logout user'),
)
