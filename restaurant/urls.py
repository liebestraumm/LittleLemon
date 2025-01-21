from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>', views.SingleMenuView.as_view(), name='single-menu-items')
]