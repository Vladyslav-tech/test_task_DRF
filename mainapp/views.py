from rest_framework import generics, filters
from django_filters import rest_framework

from .serializers import CompanyListSerializer, CompanyDetailSerializer, ProductDetailSerializer, ProductListSerializer
from .models import Company, Product



class OrganizationFilterSet(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='product__price', lookup_expr='gte', label='Min price')
    max_price = rest_framework.NumberFilter(field_name='product__price', lookup_expr='lte', label='Max price')

    class Meta:
        model = Company
        fields = ['max_price', 'min_price', 'product__category']


class Organization(generics.ListAPIView):
    serializer_class = CompanyListSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = OrganizationFilterSet
    search_fields = ['name', 'product__name']

    def get_queryset(self):
        return Company.objects.filter(districts__id=self.kwargs['pk']).distinct()



class OrganizationListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = OrganizationFilterSet


class OrganizationDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price', lookup_expr='lte', label='Minimum price')

    class Meta:
        model = Product
        fields = ['max_price', 'min_price']

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter)
    filterset_class =ProductFilter
    search_fields = ['name', 'category__name']
