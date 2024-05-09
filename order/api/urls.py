from django.urls import path

from order.api.views import OrderCreateView, ChatLinksAPIView

urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='create_order'),
    path('chat_links/', ChatLinksAPIView.as_view(), name='chat_links'),

]
