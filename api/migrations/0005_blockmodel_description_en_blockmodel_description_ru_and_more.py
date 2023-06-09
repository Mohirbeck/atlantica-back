# Generated by Django 4.2 on 2023-04-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_blockmodel_consultmodel_footermodel_partnermodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='blockmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='blockmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='blockmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='blockmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='blockmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='consultmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='consultmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='consultmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='consultmodel',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='consultmodel',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='consultmodel',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='footermodel',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='footermodel',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='footermodel',
            name='text_uz',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Отзыв'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Отзыв'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Отзыв'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='position_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='position_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='reviewmodel',
            name='position_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Должность'),
        ),
    ]
