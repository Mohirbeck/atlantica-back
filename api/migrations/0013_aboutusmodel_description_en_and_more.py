# Generated by Django 4.2 on 2023-04-19 09:14

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_aboutusmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutusmodel',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='aboutusmodel',
            name='description_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='aboutusmodel',
            name='description_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='aboutusmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='aboutusmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='aboutusmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]