from rest_framework import serializers
from catalog.models import Product, Size, Color, Tag, Variant, VariantMedia, Characteristic
from order.models import TelegramSettings, WhatsAppSettings


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('key', 'value')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'size',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('color',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)


class VariantMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantMedia
        fields = ('id', 'media')


class VariantSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    size = SizeSerializer(many=True)
    media = VariantMediaSerializer(many=True)

    class Meta:
        model = Variant
        fields = ('id', 'color', 'size', 'media')


class ProductListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    media = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price_kgs', 'price_kzt', 'price_rub', 'price_usd', 'price_discounted_kgs',
                  'price_discounted_kzt', 'price_discounted_rub', 'price_discounted_usd', 'is_top', 'is_new', 'tags', 'media')

    def get_media(self, obj):
        request = self.context.get('request')
        variants = obj.variants.all()
        media_urls = []
        for variant in variants:
            variant_media = variant.media.all()
            for media in variant_media:
                media_urls.append(request.build_absolute_uri(media.media.url) if request else media.media.url)
        return media_urls


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    variants = VariantSerializer(many=True)
    characteristics = CharacteristicSerializer(many=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_links(self, obj):
        telegram_settings = TelegramSettings.objects.first()
        whatsapp_settings = WhatsAppSettings.objects.first()
        telegram_link = f"https://t.me/{telegram_settings.link}?"
        whatsapp_link = f"https://wa.me/{whatsapp_settings.phone_number}?"
        return {'telegram': telegram_link, 'whatsapp': whatsapp_link}


