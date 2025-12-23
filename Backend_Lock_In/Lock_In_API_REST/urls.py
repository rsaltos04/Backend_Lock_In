from django.urls import path
from . import views

urlpatterns=[
    path('objetivo/estadistica/<int:pk>',views.get_objetivo_estadistico),
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
]