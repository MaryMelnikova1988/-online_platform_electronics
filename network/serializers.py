from rest_framework import serializers

from network.models import NetworkObject, Product


class NetworkObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkObject
        fields = '__all__'


class NetworkObjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkObject
        exclude = ['debt_supplier']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
