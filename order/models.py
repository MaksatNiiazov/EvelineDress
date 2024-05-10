from django.utils.translation import gettext_lazy as _
from django.db import models

from catalog.models import Variant, Size
from shop.models import SingletonModel


class Order(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name=_('Имя заказчика'))
    customer_phone = models.CharField(max_length=20, verbose_name=_('Телефон заказчика'))

    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, verbose_name=_('Вариант'))
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Размер'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ #{self.id} - {self.customer_name}'


class TelegramSettings(SingletonModel):
    link = models.CharField(max_length=255, verbose_name=_('Cсылка'), help_text=_('Никнейм в телеграм (то что идет после @ )'))

    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'Telegram'

    def __str__(self):
        return self.link


class WhatsAppSettings(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name=_('Номер телефона'), help_text=_('Номер телефона с кодом страны') )

    class Meta:
        verbose_name = 'WhatsApp'
        verbose_name_plural = 'WhatsApp'

    def __str__(self):
        return self.phone_number
