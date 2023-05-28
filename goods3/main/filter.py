from .models import Product
import django_filters

class ProductLaptopFilter(django_filters.FilterSet):
    laptops_name = django_filters.CharFilter(lookup_expr='icontains')
    laptops_price = django_filters.NumberFilter()
    laptops_price__gt = django_filters.NumberFilter(field_name='laptops_price', lookup_expr='gt')
    laptops_price__lt = django_filters.NumberFilter(field_name='laptops_price', lookup_expr='lt')


    class Meta:
        model = Product
        fields = ['laptops_name', 'laptops_price', 'brand_name']