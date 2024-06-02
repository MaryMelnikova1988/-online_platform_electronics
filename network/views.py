from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets

from network.models import NetworkObject, Product
from network.serializers import NetworkObjectSerializer, NetworkObjectUpdateSerializer, ProductSerializer
from users.permissions import IsActiveUser


class ObjectCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkObjectSerializer
    permission_classes = [IsActiveUser]


class ObjectListAPIView(generics.ListAPIView):
    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class ObjectDetailAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]


class ObjectUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkObjectUpdateSerializer
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]


class ObjectDeleteAPIView(generics.DestroyAPIView):
    queryset = NetworkObject.objects.all()
    permission_classes = [IsActiveUser]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
