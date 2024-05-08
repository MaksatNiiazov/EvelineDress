from django.urls import path

from order.api.views import OrderCreateView, ChatLinksAPIView

urlpatterns = [
    path('api/create_order/', OrderCreateView.as_view(), name='create_order'),
    path('api/chat_links/<int:pk>/', ChatLinksAPIView.as_view(), name='chat_links'),

]
