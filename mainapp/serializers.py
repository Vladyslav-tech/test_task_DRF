from rest_framework import serializers
from .models import Company, Product

class CompanyListSerializer(serializers.ModelSerializer):
    network = serializers.SlugRelatedField(slug_field='name', read_only=True)
    districts = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Company
        fields = ('name', 'network', 'districts', 'discription')

class CompanyDetailSerializer(serializers.ModelSerializer):
    network = serializers.SlugRelatedField(slug_field='name', read_only=True)
    districts = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    product = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Company
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

