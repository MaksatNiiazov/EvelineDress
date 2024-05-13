# Generated by Django 5.0.6 on 2024-05-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_wholesalerinfo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagemodel',
            name='all_products_gif',
            field=models.FileField(blank=True, null=True, upload_to='gifs', verbose_name='Гифка'),
        ),
        migrations.AddField(
            model_name='mainpagemodel',
            name='bestsellers_gif',
            field=models.FileField(blank=True, null=True, upload_to='gifs', verbose_name='Гифка'),
        ),
        migrations.AddField(
            model_name='mainpagemodel',
            name='discount_gif',
            field=models.FileField(blank=True, null=True, upload_to='gifs', verbose_name='Гифка'),
        ),
    ]