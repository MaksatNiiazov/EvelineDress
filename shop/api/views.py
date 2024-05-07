from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from shop.api.utils import create_main_page_data, create_main_page_slides, create_about_page_data, \
    create_wholesaler_info_data, create_payment_info_data, create_delivery_info_data
from shop.models import MainPageModel, MainPageSlide, AboutPageModel, PaymentInfo, WholesalerInfo, DeliveryInfo, \
    ContactInfo, Address, WorkSchedule, SocialLink, Phone
from shop.api.serializers import MainPageSerializer, MainPageSlideSerializer, AboutPageModelSerializer, \
    PaymentInfoSerializer, DeliveryInfoSerializer, WholesalerInfoSerializer, ContactInfoSerializer, AddressSerializer, \
    WorkScheduleSerializer, PhoneSerializer, SocialLinkSerializer


class MainPageAPIView(APIView):
    def get(self, request, format=None):
        main_page, created = MainPageModel.objects.get_or_create(pk=1)

        if created:
            create_main_page_data(main_page)
            create_main_page_slides(main_page)
            main_page.save()

        slides = MainPageSlide.objects.filter(page=main_page)
        main_page_serializer = MainPageSerializer(main_page, context={'request': request})
        slides_serializer = MainPageSlideSerializer(slides, many=True, context={'request': request})

        main_page_serializer.data['meta_image'] = request.build_absolute_uri(
            main_page.meta_image.url) if main_page.meta_image else ''
        main_page_serializer.data['content_image'] = request.build_absolute_uri(
            main_page.content_image.url) if main_page.content_image else ''

        return Response({
            'main_page': main_page_serializer.data,
            'slides': slides_serializer.data,
        })


class AboutPageAPIView(APIView):
    def get(self, request, format=None):
        about_page, created = AboutPageModel.objects.get_or_create(pk=1)
        if created:
            create_about_page_data(about_page)
            about_page.save()
        about_page_serializer = AboutPageModelSerializer(about_page, context={'request': request})
        return Response({
            'about_page': about_page_serializer.data,
        })


class InfoPageAPIView(APIView):
    def get(self, request, format=None):
        wholesaler_info, created = WholesalerInfo.objects.get_or_create(pk=1)
        if created:
            create_wholesaler_info_data(wholesaler_info)
        wholesaler_info.save()

        payment_info, created = PaymentInfo.objects.get_or_create(pk=1)
        if created:
            create_payment_info_data(payment_info)
        payment_info.save()

        delivery_info, created = DeliveryInfo.objects.get_or_create(pk=1)
        if created:
            create_delivery_info_data(delivery_info)
        delivery_info.save()

        wholesaler_serializer = WholesalerInfoSerializer(wholesaler_info, context={'request': request})
        payment_serializer = PaymentInfoSerializer(payment_info)
        delivery_serializer = DeliveryInfoSerializer(delivery_info)

        return Response({
            'wholesaler_info': wholesaler_serializer.data,
            'payment_info': payment_serializer.data,
            'delivery_info': delivery_serializer.data
        })


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    def get_queryset(self):
        contact_info = ContactInfo.objects.all()
        addresses = Address.objects.all()
        work_schedules = WorkSchedule.objects.all()
        phones = Phone.objects.all()
        social_links = SocialLink.objects.all()

        return {
            'contact_info': contact_info,
            'addresses': addresses,
            'work_schedules': work_schedules,
            'phones': phones,
            'social_links': social_links,
        }

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = {
            'contact_info': ContactInfoSerializer(queryset['contact_info'], many=True).data,

        }
        return Response(serializer)