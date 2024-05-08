from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


from django.db import models

from catalog.models import Variant
from shop.models import SingletonModel


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)

    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order #{self.id} - {self.customer_name}'


class TelegramSettings(SingletonModel):
    link = models.CharField(max_length=255, verbose_name=_('Cсылка'), help_text=_('Никнейм в телеграм (то что идет после @ )'))

    class Meta:
        verbose_name = 'Telegram Settings'
        verbose_name_plural = 'Telegram Settings'

    def __str__(self):
        return self.link


class WhatsAppSettings(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name=_('Номер телефона'), help_text=_('Номер телефона с кодом страны') )

    class Meta:
        verbose_name = 'WhatsApp Settings'
        verbose_name_plural = 'WhatsApp Settings'

    def __str__(self):
        return self.phone_number
