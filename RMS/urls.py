from django.urls import path
from . import views

urlpatterns=[
    path('adminProfile', views.adminProfile, name='adminProfile'),
    path('managerProfile', views.managerProfile, name='managerProfile'),
    path('logout',views.logout,name='logout'),
]