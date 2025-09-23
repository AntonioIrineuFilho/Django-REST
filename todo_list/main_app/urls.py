from django.urls import path
from .views import UserRegisterAPIView, UserLoginAPIView, TaskAPIView

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("tasks/", TaskAPIView.as_view(), name="tasks")
]