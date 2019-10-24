from django.contrib import admin
from django.urls import path
from . import views

app_name = 'sprintbacklog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addsprint/', views.add_sprint, name="addsprint"),
]
