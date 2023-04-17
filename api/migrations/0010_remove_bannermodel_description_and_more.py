# Generated by Django 4.2 on 2023-04-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_bannermodel_image_bannermodel_image_desktop_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannermodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='image_desktop',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='image_mobile',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='title',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='bannermodel',
            name='title_uz',
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='image',
            field=models.ImageField(default='', upload_to='banners', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='image_en',
            field=models.ImageField(null=True, upload_to='banners', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='image_ru',
            field=models.ImageField(null=True, upload_to='banners', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='image_uz',
            field=models.ImageField(null=True, upload_to='banners', verbose_name='Изображение'),
        ),
    ]