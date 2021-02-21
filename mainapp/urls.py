from django.urls import path
from .views import OrganizationListView, OrganizationDetailView, ProductDetailView, ProductListView,Organization


app_name = 'mainapp'

urlpatterns = [
    path('organizations/', OrganizationListView.as_view()),
    path('organization/<int:pk>/', OrganizationDetailView.as_view()),
    path('organizations/<int:pk>/', Organization.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('products/', ProductListView.as_view()),
]