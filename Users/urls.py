from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('registerskills/', views.registerSkills, name="register2"),
    path('', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('perfil/', views.perfil, name="perfil"),
    path('update/', views.update, name="editarPerfil"),
    path('ranges/', views.ranges, name="rangos"),
    path('changePassword/', views.cambiarContra, name="cambiarContra"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]