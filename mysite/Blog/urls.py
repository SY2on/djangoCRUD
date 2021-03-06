from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from Blog import views

urlpatterns = [
    path('', views.index, name = 'page-list'),
    path('create/', views.create, name = 'page-create'),
    path('detail/<int:page_id>', views.detail, name = 'page-detail'),
    path('delete/<int:page_id>', views.delete, name = 'page-delete'),
    path('update/<int:page_id>', views.update, name = 'page-update')
]
