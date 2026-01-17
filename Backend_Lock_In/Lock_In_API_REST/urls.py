from django.urls import path, include
from . import views

urlpatterns=[
    path('estadistica/<int:pk>',views.get_estadisticas),
    path('objetivo/data',views.get_all_objetivo),
    path('objetivo/get/<int:pk>',views.get_objetivo),
    path('objetivo/create',views.create_objetivo),
    path('objetivo/delete/<int:pk>',views.delete_objetivo),
    path('objetivo/put/<int:pk>',views.put_objetivo),
    path('post/data', views.get_all_post),
    path('post/get/<int:pk>', views.get_post),
    path('post/create', views.create_post),
    path('post/delete/<int:pk>', views.delete_post),
    path('post/put/<int:pk>', views.put_post),
    path('sesion_enfoque/data', views.get_all_sesion_enfoque),
    path('sesion_enfoque/get/<int:pk>', views.get_sesion_enfoque),
    path('sesion_enfoque/create', views.create_sesion_enfoque),
    path('sesion_enfoque/delete/<int:pk>', views.delete_sesion_enfoque),
    path('sesion_enfoque/put/<int:pk>', views.put_sesion_enfoque),
    path('corazon/data', views.get_all_corazones),
    path('corazon/get/<int:pk>', views.get_corazon),
    path('corazon/create', views.create_corazon),
    path('corazon/delete/<int:pk>', views.delete_corazon),
    path('corazon/put/<int:pk>', views.put_corazon),
    path('autenticacion/register/', views.register),
    path('autenticacion/login/', views.login),
    path('autenticacion/test_token/', views.test_token),
    
]