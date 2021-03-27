from django.contrib import admin
from django.urls import path

from WorkoutsApp import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('', views.index, name="index"),
]


