from django.contrib import admin
from .models import District, ProductCategory, Company, NetworkOfCompany, Product


admin.site.register(ProductCategory)


class CompanyInlineDistrict(admin.TabularInline):
    model = Company.districts.through
    verbose_name_plural = 'Редактирование данных о районе'


class CompanyInlineProduct(admin.TabularInline):
    model = Company.product.through
    verbose_name_plural = 'Редактирование данных о продукте'



class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyInlineDistrict, CompanyInlineProduct]
    exclude = ('districts', 'product')
    list_display = ('name', 'network', 'display_districts', 'discription')
    fields = ('name', 'network', 'discription')


class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = ('name',)

class NetworkAdmin(admin.ModelAdmin):
    model = NetworkOfCompany
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')


admin.site.register(Company, CompanyAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(NetworkOfCompany, NetworkAdmin)
admin.site.register(Product, ProductAdmin)





