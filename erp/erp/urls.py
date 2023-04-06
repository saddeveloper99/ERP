from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.product_list_view, name='')
]