from rest_framework import serializers
from shop.models import MainPageModel, MainPageSlide, AdvantageModel, ReviewModel, AboutPageModel, WholesalerProduct, \
    PaymentInfo, DeliveryInfo, WholesalerInfo, SocialLink, Phone, WorkSchedule, Address, ContactInfo


class MainPageSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageSlide
        fields = ('id', 'slide')


class MainPageSerializer(serializers.ModelSerializer):
    slides = MainPageSlideSerializer(many=True, read_only=True)

    class Meta:
        model = MainPageModel
        fields = ('id', 'keywords', 'meta_title', 'meta_description', 'meta_image', 'title1', 'title2', 'title3',
                  'content_title', 'content_text', 'bestsellers_tittle', 'discount_tittle', 'all_products_title', 'content_image', 'slides')


class AdvantageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantageModel
        fields = '__all__'


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'


class AboutPageModelSerializer(serializers.ModelSerializer):
    advantages = AdvantageModelSerializer(many=True, read_only=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = AboutPageModel
        fields = '__all__'

    def get_reviews(self, obj):
        request = self.context.get('request')
        print(request)
        reviews = obj.reviews.all()
        return [
            request.build_absolute_uri(review.review.url) if request else review.review.url
            for review in reviews
        ]


class WholesalerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholesalerProduct
        fields = ('image', 'text')


class WholesalerInfoSerializer(serializers.ModelSerializer):
    products = WholesalerProductSerializer(many=True, read_only=True)

    class Meta:
        model = WholesalerInfo
        fields = '__all__'


class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = '__all__'


class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    work_schedules = WorkScheduleSerializer(many=True)
    phones = PhoneSerializer(many=True)
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = ContactInfo
        fields = '__all__'
