from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.models import Variant, Size
from order.api.forms import ChatLinksForm
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

