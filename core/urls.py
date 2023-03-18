from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  #Remove this when you have your own home URL
    path('admin/login/', views.LoginView.as_view()),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]


