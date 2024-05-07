from django.urls import path

from shop.api.views import MainPageAPIView, AboutPageAPIView, InfoPageAPIView, ContactInfoAPIView

urlpatterns = [
    path('main-page/', MainPageAPIView.as_view(), name='main-page-api'),
    path('about/', AboutPageAPIView.as_view(), name='about-page-api'),
    path('info/', InfoPageAPIView.as_view(), name='info-page-api'),
    path('contacts/', ContactInfoAPIView.as_view(), name='contact_info'),

]