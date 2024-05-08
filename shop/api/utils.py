from django.conf import settings
from django.core.files import File
import os

from shop.models import MainPageSlide, AdvantageModel, ReviewModel, WholesalerProduct, SocialLink, Address, \
    WorkSchedule, Phone


def create_main_page_data(main_page):
    main_page.meta_title = 'Default Meta Title'
    main_page.meta_description = 'Default Meta Description'
    main_page.title1 = 'Сияйте'
    main_page.title2 = 'на выпускном'
    main_page.title3 = 'в наших платьях'
    main_page.content_title = 'Привет, меня зовут Фатимаи Я основательница бренда Evelin'
    main_page.content_text = '''
    В 2021 году Я столкнулась с проблемой поиска платья на свой выпускной вечер
    Представляла выпускной в стиле American style, но к сожалению на тот момент нигде не продавали шелковые платья в стиле минимализм
    Я поняла, как сложно найти идеальное платье своей мечты, и поэтому...
    Решила открыть свой магазин вечерних платьев как из Pinterest
    На сегодняшний день, мы сшили более 2 000 роскошных нарядов 
    '''
    main_page.bestsellers_tittle = 'Наши бестселлеры'
    main_page.discount_tittle = 'Скидки'
    main_page.all_products_title = 'Все платья'
    content_image_path = 'assets/mainpage/content_image.png'
    with open(os.path.join(settings.BASE_DIR, content_image_path), 'rb') as content_image_file:
        main_page.content_image.save(os.path.basename(content_image_path), File(content_image_file), save=True)


def create_main_page_slides(main_page):
    slide_image_path1 = 'assets/mainpage/slider/default_slide1.png'
    with open(os.path.join(settings.BASE_DIR, slide_image_path1), 'rb') as slide_image_file1:
        slide1 = MainPageSlide.objects.create(page=main_page)
        slide1.slide.save(os.path.basename(slide_image_path1), File(slide_image_file1), save=True)

    slide_image_path2 = 'assets/mainpage/slider/default_slide2.png'
    with open(os.path.join(settings.BASE_DIR, slide_image_path2), 'rb') as slide_image_file2:
        slide2 = MainPageSlide.objects.create(page=main_page)
        slide2.slide.save(os.path.basename(slide_image_path2), File(slide_image_file2), save=True)


def create_about_page_data(about_page):
    about_page.title = 'Привет, меня зовут Фатима и Я основательница бренда Evelin'
    about_page.text = '''
    В 2021 году Я столкнулась с проблемой поиска платья на свой выпускной вечер
    Представляла выпускной в стиле American style, но к сожалению на тот момент нигде не продавали шелковые платья в стиле минимализм
    Я поняла, как сложно найти идеальное платье своей мечты, и поэтому...
    Решила открыть свой магазин вечерних платьев как из Pinterest
    На сегодняшний день, мы сшили более 2 000 роскошных нарядов 
    '''
    about_page.advantages_title = 'Почему Evelin - лучший выбор платьев на выпускной?'
    about_page.reviews_title = 'Чтобы еще больше убедиться в качестве наших товаров, посмотрите отзывы наших покупательниц'
    content_image_path = 'assets/mainpage/content_image.png'
    with open(os.path.join(settings.BASE_DIR, content_image_path), 'rb') as content_image_file:
        about_page.image.save(os.path.basename(content_image_path), File(content_image_file), save=True)

    AdvantageModel.objects.create(
        page=about_page,
        title='Эксклюзивный дизайн',
        content_text='Наши платья созданы с учетом последних тенденций моды'
    )
    AdvantageModel.objects.create(
        page=about_page,
        title='Надежное качество',
        content_text='Мы используем только лучшие материалы и следим за каждой деталью'
    )
    AdvantageModel.objects.create(
        page=about_page,
        title='Поддержка клиентов',
        content_text='Наша дружелюбная команда всегда готова помочь вам с выбором'
    )
    AdvantageModel.objects.create(
        page=about_page,
        title='Широкий ассортимент',
        content_text='Мы предлагаем разнообразие стилей, размеров и цветов'
    )

    reviews = [
        'assets/reviews/review1.png', 'assets/reviews/review2.png', 'assets/reviews/review3.png',
        'assets/reviews/review4.png', 'assets/reviews/review5.png'
    ]

    for review_path in reviews:
        try:
            with open(os.path.join(settings.BASE_DIR, review_path), 'rb') as image_file:
                review = ReviewModel(page=about_page)
                review.review.save(os.path.basename(review_path), File(image_file), save=True)
        except Exception as e:
            print(f"Error creating review: {e}")


def create_wholesaler_info_data(wholesaler_info):
    wholesaler_info.text = 'Для того чтобы оформить заказ вам необходимо:  1. Указать Фио ( при получении обязательно подойти в' \
           ' офис с паспортом ! )    2. Уточнить своё платюшко в наличии ли ( свой размер, расцветок )' \
           '   3. Указать ближайший адрес пункта Сдэка ( отправляем до офиса )   4. Обязательно указать' \
           ' номер телефона и ещё дополнительный ( в случаи если не возьмете трубку )   5. Оплатить сумму' \
           ' платья 100% на  оптиму 4169585355558379  Syrgabaeva Fatima Syrgabaevna'
    wholesaler_info.additional_text = 'Внимание! Перед тем как оплатить за пять минут ещё раз удостоверьтесь что в наличии есть ли' \
                      ' платья ( так как платье могут купить даже за пять минут пока вы думаете )'
    wholesaler_info.button_text = 'Связаться с менеджером'
    wholesaler_info.button_link = '#'

    image_path = 'assets/wholesaler_product/product.png'

    with open(image_path, 'rb') as image_file:
        WholesalerProduct.objects.create(
            wholesaler_info=wholesaler_info,
            image=File(image_file),
            text='Платье «SAXAR» - наш абсолютный бестселлер ❤️‍🔥 Платье, на которое есть огромный спрос уже'
                 ' второй год. Отшиваем очень редко, только в период выпускного.'
        )

def create_payment_info_data(payment_info):
    payment_info.title = 'Для того чтобы оформить заказ вам необходимо:'
    payment_info.text = 'Для того чтобы оформить заказ вам необходимо:  1. Указать Фио ( при получении обязательно подойти в офис с паспортом ! )    2. Уточнить своё платюшко в наличии ли ( свой размер, расцветок )  3. Указать ближайший адрес пункта Сдэка ( отправляем до офиса )  4. Обязательно указать номер телефона и ещё дополнительный ( в случаи если не возьмете трубку )  5. Оплатить сумму платья 100% на  оптиму 4169585355558379 Syrgabaeva Fatima Syrgabaevna'
    payment_info.additional_text = 'Внимание! Перед тем как оплатить за пять минут ещё раз удостоверьтесь что в наличии есть ли платья ( так как платье могут купить даже за пять минут пока вы думаете )'


def create_delivery_info_data(delivery_info):
    delivery_info.title = 'Доставка и возврат'
    delivery_info.text = 'Доставка в другие страны осуществляются через курьерскую службу СДЭК   Наземная доставка в течении 2-4 недель 1000 руб  Авиа доставка в течении 3-6 рабочих дней 3000 руб За доставку оплачиваете сразу нам  После оплаты мы в течении дня отправляем трек, где вы можете отследить свой заказ  https://www.cdek.ru/ru ( отследить можете через этот сайт )  Внимание! Перед тем как оплатить за пять минут ещё раз удостоверьтесь что в наличии есть ли платья ( так как платье могут купить даже за пять минут пока вы думаете )'



def create_social_link_data(contact_info):
    social_links_data = [
        {
            'name': 'WhatsApp',
            'logo': 'assets/sociallinks/whatsapp.svg',
            'url': ''
        },
        {
            'name': 'Instagram',
            'logo': 'assets/sociallinks/instagram.svg',
            'url': ''
        },
        {
            'name': 'TikTok',
            'logo': 'assets/sociallinks/tiktok.svg',
            'url': ''
        },
        {
            'name': 'Telegram',
            'logo': 'assets/sociallinks/telegram.svg',
            'url': ''
        },

    ]
    social_links = []
    for data in social_links_data:
        try:
            logo_path = os.path.join(settings.BASE_DIR, data['logo'])
            with open(logo_path, 'rb') as image_file:
                social_link = SocialLink(
                    contact_info=contact_info,
                    name=data['name'],
                    url=data['url']
                )
                social_link.logo.save(os.path.basename(data['logo']), File(image_file), save=True)
                social_links.append(social_link)
        except Exception as e:
            print(f"Error creating social link: {e}")
    return social_links


def create_contact_info_data(contact_info):
    addresses = Address.objects.all()
    if not addresses:
        Address.objects.create(contact_info=contact_info, address='Адрес: ул. Киевская 62, ТЦ “Евразия”'
                                                                              ' 3 этаж, бутик COLLAB')
    work_schedules = WorkSchedule.objects.all()
    if not work_schedules:
        WorkSchedule.objects.create(contact_info=contact_info)
    phones = Phone.objects.all()
    if not phones:
         Phone.objects.create(contact_info=contact_info, phone='Для заказа WhatsApp: +996 (502) 431-428')
    social_links = SocialLink.objects.all()
    if not social_links:
        create_social_link_data(contact_info)
