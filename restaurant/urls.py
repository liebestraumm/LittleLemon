from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # The api-auth route is defined to let you use the browsable API feature of DRF.  
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('items/', views.MenuItemView.as_view(), name='menu-items'),
    path('items/<int:pk>', views.SingleMenuView.as_view(), name='single-menu-items'),
    *router.urls
]