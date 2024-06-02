from django.urls import path
from rest_framework.routers import DefaultRouter

from network.apps import NetworkConfig
from network.views import ObjectListAPIView, ObjectDetailAPIView, ObjectCreateAPIView, ObjectUpdateAPIView, \
    ObjectDeleteAPIView, ProductViewSet

app_name = NetworkConfig.name
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('list/', ObjectListAPIView.as_view(), name='object_list'),
    path('<int:pk>/', ObjectDetailAPIView.as_view(), name='object_detail'),
    path('create/', ObjectCreateAPIView.as_view(), name='object_create'),
    path('update/<int:pk>/', ObjectUpdateAPIView.as_view(), name='object_update'),
    path('delete/<int:pk>/', ObjectDeleteAPIView.as_view(), name='object_delete'),
] + router.urls
