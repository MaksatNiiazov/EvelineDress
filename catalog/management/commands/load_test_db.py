import os
import shutil
import string
import random
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.files import File as DjangoFile
from faker import Faker
from catalog.models import Product, Characteristic, Size, Color, Tag, Variant, VariantMedia

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with random data'

    def handle(self, *args, **kwargs):
        self.create_products()

    def get_random_image_path(self):
        images_path = Path(settings.BASE_DIR) / 'assets' / 'products'
        image_files = [f for f in images_path.iterdir() if f.is_file()]
        return random.choice(image_files) if image_files else None

    def generate_random_filename(self, length=10):
        """Generate a random filename of the specified length."""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def create_products(self):
        for _ in range(10):  # Create 10 products
            product = Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                price_kgs=random.randint(100, 1000),
                price_kzt=random.randint(1000, 10000),
                price_rub=random.randint(100, 1000),
                price_usd=random.randint(1, 10),
                price_discounted_kgs=random.randint(50, 500),
                price_discounted_kzt=random.randint(500, 5000),
                price_discounted_rub=random.randint(50, 500),
                price_discounted_usd=random.randint(1, 5),
                is_top=fake.boolean(),
                is_new=fake.boolean()
            )

            # Create random characteristics for the product
            for _ in range(5):
                Characteristic.objects.create(
                    key=fake.word(),
                    value=fake.word(),
                    product=product
                )

            # Create random variants for the product
            for _ in range(3):
                variant = Variant.objects.create(
                    product=product,
                    color=Color.objects.create(color=fake.color_name()),
                    size=Size.objects.create(size=fake.word()),
                )

                # Load random media for the product variant
                image_path = self.get_random_image_path()
                if image_path:
                    # Create a new file name for the image
                    image_name = f"{self.generate_random_filename(10)}.jpg"
                    image_dest_path = Path(settings.MEDIA_ROOT) / 'products_media' / image_name

                    # Copy the image file to the media directory
                    shutil.copy(image_path, image_dest_path)

                    # Create VariantMedia object with the copied file
                    VariantMedia.objects.create(
                        variant=variant,
                        media=f'products_media/{image_name}'
                    )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with random data.'))
