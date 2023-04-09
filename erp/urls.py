from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_list/', views.product_list_view, name='product-list'),
    path('inbound_create/', views.inbound_create, name='inbound-create'),
    path('outbound_create/', views.outbound_create, name='outbound-create'),
]