from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Company, District, Product, ProductCategory, NetworkOfCompany
from django.forms.models import model_to_dict

class APITests(APITestCase):

    def setUp(self):
        districts_1 = District.objects.create(name='Московский')
        districts_2 = District.objects.create(name='Центральный')
        product_category = ProductCategory.objects.create(name='TV')
        product = Product.objects.create(name='Samsung_2020',
                                         category=product_category,
                                         price=10000)
        network = NetworkOfCompany.objects.create(name='DNS')

        company_1 = Company.objects.create(name='Company_1',
                                           network=network,
                                           )
        company_1.districts.add(districts_1)
        company_1.product.add(product)

        company_2 = Company.objects.create(name='Company_2',
                                           network=network)
        company_2.districts.add(districts_2)
        company_2.product.add(product)




    def test_organizations_url(self):
        """Testing organizations list url"""
        response = self.client.get(reverse('api_views:org_list'), format='json')
        self.assertEqual(response.status_code, 200)

    def test_organization_detail_url(self):
        """Testing organization details urls"""
        for company in Company.objects.all():
            response = self.client.get(reverse('api_views:org_detail', kwargs={'pk':company.pk}))
            qs = Company.objects.get(pk=company.pk)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['name'], qs.name)
            self.assertEqual(response.data['network'], qs.network.name)

    def test_organizations_district_pk_url(self):
        """Testing organization urls by district_pk"""
        for district in District.objects.all():
            response = self.client.get(reverse('api_views:org_district_pk', kwargs={'pk':district.pk}))
            qs = Company.objects.get(districts__pk=district.pk)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()[0].get('name'), qs.name)
            self.assertEqual(response.json()[0].get('network'), qs.network.name)


    def test_product_url(self):
        """Testing products list url"""
        response = self.client.get(reverse('api_views:products_list'), format='json')
        self.assertEqual(response.status_code, 200)

    def test_products_detail_url(self):
        """Testing product details urls"""
        for product in Product.objects.all():
            response = self.client.get(reverse('api_views:product_detail', kwargs={'pk': product.pk}))
            qs = Product.objects.get(pk=product.pk)
            qs_dct = model_to_dict(qs)
            qs_dct['category'] = 'TV'
            print(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(qs_dct, response.data)




