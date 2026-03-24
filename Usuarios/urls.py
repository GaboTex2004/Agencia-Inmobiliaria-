from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, login, register

router = DefaultRouter()
router.register(r'Usuarios', UsuarioViewSet)

urlpatterns = [
    path("login/", login),
    path("register/", register),
    path("",include(router.urls)),
]