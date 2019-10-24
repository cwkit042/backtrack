from django.contrib import admin
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addproduct/', views.add_product, name="addproduct"),
    path('', views.pbi_list, name="pbilist"),
    path('addpbi/', views.add_pbi, name="addpbi"),
]
