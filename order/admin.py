from django.contrib import admin
from .models import Order, TelegramSettings, WhatsAppSettings


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_phone', 'variant', 'size', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_name', 'customer_phone')


admin.site.register(WhatsAppSettings)
admin.site.register(TelegramSettings)
