from datetime import time

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists():
            existing_instance = self.__class__.objects.get()
            self.id = existing_instance.id
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            return cls.objects.create()
        return cls.objects.get()


class MainPageModel(SingletonModel):
    keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Мета-заголовок'))
    meta_description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Мета-описание'))
    meta_image = models.FileField(upload_to='meta_images', blank=True, null=True, default='assets/icons/LOGO.svg')
    title1 = models.CharField(max_length=255, verbose_name=_('Строка 1'))
    title2 = models.CharField(max_length=255, verbose_name=_('Строка 2'))
    title3 = models.CharField(max_length=255, verbose_name=_('Строка 3'))

    content_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Заголовок текста'))
    content_text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))
    content_image = models.ImageField(upload_to='main_page', blank=True, null=True,
                                      default='assets/mainpage/content_image.png', verbose_name=_('Изображение'))
    bestsellers_tittle = models.CharField(max_length=255, blank=True, null=True,
                                          verbose_name=_('Бестселлеры заголовок'))
    discount_tittle = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Скидки заголовок'))
    all_products_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Все товары заголовок'))

    class Meta:
        verbose_name = 'Контент главной страницы'
        verbose_name_plural = 'Контент главной страницы'

    def __str__(self):
        return 'Главная страница'

    def save(self, *args, **kwargs):
        if not self.meta_title:
            self.meta_title = f'{self.title1} {self.title2} {self.title3}'
        if not self.meta_description:
            self.meta_description = f'{self.title1} {self.title2} {self.title3}'
        super(MainPageModel, self).save(*args, **kwargs)


class MainPageSlide(models.Model):
    page = models.ForeignKey(MainPageModel, on_delete=models.CASCADE, verbose_name='slides')
    slide = models.ImageField(upload_to='main_slider')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слыйды'


class AboutPageModel(SingletonModel):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Заголовок'))
    text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))
    image = models.ImageField(upload_to='main_page', blank=True, null=True, verbose_name=_('Изображение'))
    advantages_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Приемущества заголовок'))
    reviews_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Отзывы заголовок'))

    class Meta:
        verbose_name = 'Контент страницы "О нас"'
        verbose_name_plural = 'Контент страницы "О нас"'

    def __str__(self):
        return "О нас"


class AdvantageModel(models.Model):
    page = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE, related_name='advantages')
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    content_text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))

    class Meta:
        verbose_name = 'Приемущество'
        verbose_name_plural = 'Приемущества'


class ReviewModel(models.Model):
    page = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE, related_name='reviews')
    review = models.ImageField(upload_to='reviews', verbose_name=_('Отзыв'))

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class WholesalerInfo(SingletonModel):
    text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))
    additional_text = models.TextField(blank=True, null=True, verbose_name=_('Дополнительный текст'))
    button_text = models.CharField(max_length=100, verbose_name=_('Текст кнопки'))
    button_link = models.URLField(blank=True, null=True, verbose_name=_('Ссылка'))

    class Meta:
        verbose_name = 'Оптовикам'
        verbose_name_plural = 'Оптовикам'

    def __str__(self):
        return "Информация оптовикам"


class WholesalerProduct(models.Model):
    wholesaler_info = models.ForeignKey(WholesalerInfo, on_delete=models.PROTECT, related_name='products')
    image = models.ImageField(upload_to='wholesaler_images')
    text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class PaymentInfo(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))
    additional_text = models.TextField(blank=True, null=True, verbose_name=_('Дополнительный текст'))

    class Meta:
        verbose_name = 'Об оплате'
        verbose_name_plural = 'Об оплате'

    def __str__(self):
        return self.title


class DeliveryInfo(SingletonModel):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    text = models.TextField(blank=True, null=True, verbose_name=_('Текст'))

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставка'

    def __str__(self):
        return self.title


class ContactInfo(SingletonModel):
    pass

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return "Контактная информация"


class Address(models.Model):
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.PROTECT, related_name='addresses')
    address = models.TextField(verbose_name=_('Адрес'))

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address


class WorkSchedule(models.Model):
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.PROTECT, related_name='work_schedules')
    text = models.CharField(max_length=255, blank=True, null=True, help_text='Дни когда это время актуально (можно '
                                                                             'оставить пустым)')
    start = models.TimeField(default=time(10, 0, 0).replace(second=0, microsecond=0))
    end = models.TimeField(default=time(10, 0, 0).replace(second=0, microsecond=0))

    class Meta:
        verbose_name = 'Рабочее время'
        verbose_name_plural = 'Рабочее время'

    def __str__(self):
        return f'{self.start} : {self.end}'


class Phone(models.Model):
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.PROTECT, related_name='phones')
    phone = models.CharField(max_length=255, verbose_name=_('Телефон'))

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.phone


class SocialLink(models.Model):
    contact_info = models.ForeignKey(ContactInfo, on_delete=models.PROTECT, related_name='social_links')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Соцсети'))
    logo = models.FileField(upload_to='social_link_logo', blank=True, null=True, verbose_name=_('Логотип'))
    url = models.URLField(blank=True, null=True, verbose_name=_('Ссылка'))

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'

    def __str__(self):
        return self.name


class SiteContent(models.Model):
    original_text = models.TextField(verbose_name="Оригинальный текст",
                                     help_text="Оригинальный текст, который отображается на сайте.",
                                     max_length=20000
                                     )
    current_text = models.TextField(
        verbose_name="Текущий текст",
        help_text="Измененный или текущий текст, который отображается на сайте.",
        max_length=20000
    )

    class Meta:
        verbose_name = "Контент сайта"
        verbose_name_plural = "Контент сайта"
