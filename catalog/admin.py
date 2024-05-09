from django.contrib import admin
from django.utils.safestring import mark_safe
from nested_admin.nested import NestedStackedInline, NestedModelAdmin

from catalog.models import Product, Size, Color, Variant, VariantMedia, Characteristic, Tag


class VariantMediaInline(NestedStackedInline):
    model = VariantMedia
    extra = 1
    readonly_fields = ("get_media",)

    def get_media(self, obj):
        return mark_safe(f'<img src = {obj.media.url} width = "300"')


class VariantInline(NestedStackedInline):
    model = Variant
    extra = 0
    inlines = [VariantMediaInline]


class CharacteristicInline(NestedStackedInline):
    model = Characteristic
    extra = 0



class ProductAdmin(NestedModelAdmin):
    inlines = [VariantInline, CharacteristicInline]
    list_display = ('name', 'price', 'is_active')
    search_fields = ['name']
    filter_horizontal = ['tags']

    def price(self, obj):
        return f"{obj.price_kgs} KGS, {obj.price_kzt} KZT, {obj.price_rub} RUB, {obj.price_usd} USD"

    fieldsets = [
        ('Main Information', {'fields': ['is_active', 'name', 'is_new', 'is_top', 'description', 'tags', 'price_kgs', 'price_kzt',
                                         'price_rub', 'price_usd', 'price_discounted_kgs', 'price_discounted_kzt',
                                         'price_discounted_rub', 'price_discounted_usd']}),
        ('SEO Information', {'fields': ['keywords', 'meta_title', 'meta_description'], 'classes': ['collapse']}),
    ]



admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(Variant)
admin.site.register(VariantMedia)
