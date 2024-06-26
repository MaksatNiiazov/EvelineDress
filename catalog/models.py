from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    name = models.CharField(max_length=255, verbose_name=_('Продукт'))
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    tags = models.ManyToManyField('Tag', related_name='products', blank=True, null=True, verbose_name=_('Тэги'))
    is_active = models.BooleanField(default=True, verbose_name=_('Активность'))
    price_kgs = models.PositiveIntegerField(verbose_name=_('Цена в сомах'))
    price_kzt = models.PositiveIntegerField(verbose_name=_('Цена в тенге'))
    price_rub = models.PositiveIntegerField(verbose_name=_('Цена в рублях'))
    price_usd = models.PositiveIntegerField(verbose_name=_('Цена в долларах'))
    price_discounted_kgs = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Скидочная цена в сомах'))
    price_discounted_kzt = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Скидочная цена в тенге'))
    price_discounted_rub = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Скидочная цена в рублях'))
    price_discounted_usd = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Скидочная цена в долларах'))
    is_top = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Мета-заголовок'))
    meta_description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Мета-описание'))
    meta_image = models.FileField(upload_to='meta_images', blank=True, null=True, default='assets/icons/logo.png')



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-is_active']
    def __str__(self):
        return f'{self.name} - {self.price_kgs}с.'

    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = self.name
        if not self.meta_description:
            self.meta_description = self.description[:255] if self.description else ''
        super(Product, self).save(*args, **kwargs)


class Characteristic(models.Model):
    key = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Ключ'))
    value = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Значение'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics', verbose_name=_('Характеристика'))

    def __str__(self):
        return self.key
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Size(models.Model):
    size = models.CharField(max_length=255, verbose_name=_('Размер'))

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.size


class Color(models.Model):
    color = models.CharField(max_length=255, verbose_name=_('Цвет'))

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.color


class Tag(models.Model):
    tag = models.CharField(max_length=255, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.tag


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    size = models.ManyToManyField(Size, related_name='variants', verbose_name=_('Размер'))

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return f'{self.product.name, self.color.color}'


class VariantMedia(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='media')
    media = models.FileField(upload_to='products_media', verbose_name=_('Медиа'))

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'
