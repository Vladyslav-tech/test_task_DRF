from django.db import models


class District(models.Model):
    name = models.CharField(verbose_name='Район', max_length=64, unique=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=128, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название товара', max_length=128)
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class NetworkOfCompany(models.Model):
    name = models.CharField(verbose_name='Название Сети', max_length=128, unique=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(verbose_name='Имя компании', max_length=128)
    discription = models.TextField(verbose_name='Описание', blank=True)
    network = models.ForeignKey(NetworkOfCompany, verbose_name='Название сети', on_delete=models.CASCADE)
    districts = models.ManyToManyField(District, verbose_name='Район')
    product = models.ManyToManyField(Product, verbose_name='Имя товара')

    def display_districts(self):
        """
        Creates a list of Districts. This is required to display district in Admin panel.
        """
        return [district.name for district in self.districts.all()]
    display_districts.short_description = 'Район'

    def __str__(self):
        return f"{self.name} ({self.network.name})"
