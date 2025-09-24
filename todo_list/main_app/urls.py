from django.urls import path
from .views import UserRegisterAPIView, UserLoginAPIView, CreateReadTaskAPIView, UpdateDeleteTaskAPI

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
    path("tasks/", CreateReadTaskAPIView.as_view(), name="collection_tasks"),
    path("tasks/<int:pk>", UpdateDeleteTaskAPI.as_view(), name="individual_tasks")
]