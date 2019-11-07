from django.contrib import admin
from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register')
]
