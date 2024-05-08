from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import MainPageModel, MainPageSlide, AboutPageModel, AdvantageModel, ReviewModel, WholesalerInfo, \
    WholesalerProduct, PaymentInfo, DeliveryInfo, ContactInfo, Address, WorkSchedule, Phone, SocialLink, SiteContent


class MainPageSlideInline(admin.TabularInline):
    model = MainPageSlide
    extra = 0
    readonly_fields = ("get_media",)

    def get_media(self, obj):
        return mark_safe(f'<img src = {obj.slide.url} width = "300"')


class AdvantageModelInline(admin.TabularInline):
    model = AdvantageModel
    extra = 0


class ReviewModelInline(admin.TabularInline):
    model = ReviewModel
    extra = 0
    readonly_fields = ("get_media",)

    def get_media(self, obj):
        return mark_safe(f'<img src = {obj.review.url} width = "300"')


class WholesalerProductInline(admin.TabularInline):
    model = WholesalerProduct
    extra = 0


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class WorkScheduleInline(admin.TabularInline):
    model = WorkSchedule
    extra = 0


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 0


@admin.register(MainPageModel)
class MainPageModelAdmin(admin.ModelAdmin):
    inlines = [MainPageSlideInline]
    list_display = ['title1', 'title2', 'title3',]
    readonly_fields = ("get_media",)

    def get_media(self, obj):
        return mark_safe(f'<img src = {obj.content_image.url} width = "300"')


@admin.register(AboutPageModel)
class AboutPageModelAdmin(admin.ModelAdmin):
    inlines = [AdvantageModelInline, ReviewModelInline]
    list_display = ['title', 'image', 'advantages_title', 'reviews_title']
    readonly_fields = ("get_media",)

    def get_media(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')


@admin.register(WholesalerInfo)
class WholesalerInfoAdmin(admin.ModelAdmin):
    inlines = [WholesalerProductInline]
    list_display = ['text', 'additional_text', 'button_text', 'button_link']


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    inlines = [AddressInline, WorkScheduleInline, PhoneInline, SocialLinkInline]


admin.site.register(PaymentInfo)
admin.site.register(DeliveryInfo)
admin.site.register(SiteContent)
admin.site.register(Address)
admin.site.register(WorkSchedule)
admin.site.register(Phone)
admin.site.register(SocialLink)


