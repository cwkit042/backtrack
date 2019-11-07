from django.contrib import admin
from django.urls import path
from . import views

app_name = 'productbacklog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addproduct/', views.add_product, name="addproduct"),
    path('', views.homepage, name="pbilist"),
    #path('pbicurrentlist/', views.pbi_current_list, name="pbicurrentlist"),
    path('addpbi/', views.add_pbi, name="addpbi"),
    path('fulllist/', views.pbi_list, name="fulllist"),
    path('orderlist/', views.order_list, name="orderlist"),
    path('switchpbi', views.switch_pbi, name="switchpbi"),
    path('deletepbi/', views.delete_pbi, name="deletepbi"),
    path('modifypbi/', views.modify_pbi, name="modifypbi"),
]
