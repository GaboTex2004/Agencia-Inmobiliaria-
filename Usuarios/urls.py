from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, login

router = DefaultRouter()
router.register(r'Usuarios', UsuarioViewSet)

urlpatterns = [
    path("login/", login),
    path("",include(router.urls)),
]