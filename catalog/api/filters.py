import django_filters
from django.db.models import Q

from catalog.models import Product


class ProductFilter(django_filters.FilterSet):
    is_new = django_filters.BooleanFilter(field_name='is_new', label='Новинки')
    is_top = django_filters.BooleanFilter(field_name='is_top', label='Топ')
    has_discount = django_filters.BooleanFilter(method='filter_has_discount', label='Товары со скидкой')

    def filter_has_discount(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(price_discounted_kgs__isnull=False) |
                Q(price_discounted_kzt__isnull=False) |
                Q(price_discounted_rub__isnull=False) |
                Q(price_discounted_usd__isnull=False)
            )
        return queryset

    class Meta:
        model = Product
        fields = ['is_new', 'is_top', 'has_discount']
