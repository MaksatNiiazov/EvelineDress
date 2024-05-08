from rest_framework import generics, status
from rest_framework.response import Response

from catalog.models import Variant
from order.api.serializers import OrderSerializer
from order.models import Order, TelegramSettings, WhatsAppSettings


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChatLinksAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        variant_id = self.kwargs.get('pk')
        variant = Variant.objects.get(pk=variant_id)

        product_name = variant.product.name
        color = variant.color.color
        size = variant.size.size

        telegram_settings = TelegramSettings.objects.first()
        whatsapp_settings = WhatsAppSettings.objects.first()

        telegram_link = f"https://t.me/{telegram_settings.link}?text=Product%3A%20{product_name}%0AColor%3A%20{color}%0ASize%3A%20{size}"
        whatsapp_link = f"https://wa.me/{whatsapp_settings.phone_number}?text=Product%3A%20{product_name}%0AColor%3A%20{color}%0ASize%3A%20{size}"

        if telegram_settings and whatsapp_settings:
            return Response({'telegram_link': telegram_link, 'whatsapp_link': whatsapp_link})
        elif telegram_settings:
            return Response({'telegram_link': telegram_link})
        elif whatsapp_settings:
            return Response({'whatsapp_link': whatsapp_link})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
