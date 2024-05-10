from django.urls import path

from order.api.views import OrderCreateView

urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='create_order'),

]
