from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
