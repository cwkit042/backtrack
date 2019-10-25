from django.contrib import admin
from django.urls import path
from . import views

app_name = 'sprintbacklog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addsprintview/',views.CreateSprintView.as_view(), name="addsprintview"),
    path('', views.sprint_list, name="sprintlist"),
    path('addsbi/<int:id>/', views.add_sbi, name="addsbi"),
    path('sbilist/<int:id>/', views.sbi_list, name="sbilist"),
    path('addtask/<int:id>/', views.add_task, name="addtask"),
]
