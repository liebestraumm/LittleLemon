from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('', include(router.urls)),
    # The api-auth route is defined to let you use the browsable API feature of DRF.  
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('booking/', views.BookingView.as_view(), name='booking'),
]