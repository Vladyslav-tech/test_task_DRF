from django.urls import path
from .views import OrganizationListView, OrganizationDetailView, ProductDetailView, ProductListView,Organization

app_name = 'mainapp'

urlpatterns = [
    path('organizations/', OrganizationListView.as_view(), name='org_list'),
    path('organization/<int:pk>/', OrganizationDetailView.as_view(), name='org_detail'),
    path('organizations/<int:pk>/', Organization.as_view(), name='org_district_pk'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='products_list'),
]