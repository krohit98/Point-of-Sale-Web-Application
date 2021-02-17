from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('authManager', views.authManager, name='authManager'),
    path('authStaff', views.authStaff, name='authStaff'),
    path('loginManager', views.loginManager, name='loginManager'),
    path('loginStaff', views.loginStaff, name='loginStaff'),
    path('registerAdmin', views.registerAdmin, name='registerAdmin'),
    path('loginAdmin', views.loginAdmin, name='loginAdmin'),
]
