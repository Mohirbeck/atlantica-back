from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ValidationError

# Create your models here.

def validate_file_extension(value):
    if not value.name.endswith(".svg"):
        raise ValidationError("Только SVG файлы")

class ServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = RichTextUploadingField(verbose_name="Описание услуги", blank=True, null=True)
    icon = models.FileField(upload_to="services", verbose_name="Иконка услуги", blank=True, null=True, help_text="Рекомендуемый размер 64x64", validators=[validate_file_extension])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
class ProjectModel(models.Model):
    statuses = (
        ("В работе", "В работе"),
        ("Завершен", "Завершен"),
    )
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    description = RichTextUploadingField(verbose_name="Описание проекта", blank=True, null=True)
    image = models.ImageField(upload_to="projects", verbose_name="Изображение проекта", blank=True, null=True)
    client = models.CharField(max_length=255, verbose_name="Клиент", blank=True, null=True)
    category = models.ForeignKey("ProjectCategoryModel", on_delete=models.CASCADE, verbose_name="Категория", blank=True, null=True)
    service = models.ManyToManyField("ServiceModel", verbose_name="Услуга", blank=True)
    date = models.DateField(verbose_name="Дата", blank=True, null=True)
    status = models.CharField(max_length=255, choices=statuses, verbose_name="Статус", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
    
class ProjectCategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория проекта"
        verbose_name_plural = "Категории проектов"
    
class NewsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = RichTextUploadingField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(upload_to="news", verbose_name="Изображение", blank=True, null=True)
    views = models.BigIntegerField(verbose_name="Просмотры", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
class RequestModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")
    type = models.CharField(max_length=255, verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

class BannerModel(models.Model):
    link = models.CharField(max_length=255, verbose_name="Ссылка", blank=True, null=True)
    image = models.ImageField(upload_to="banners", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    order = models.IntegerField(verbose_name="Порядок", default=0)

    def __str__(self):
        return 'Баннер'
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

class ReviewModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    position = models.CharField(max_length=255, verbose_name="Должность")
    image = models.ImageField(upload_to="reviews", verbose_name="Изображение")
    description = models.TextField(verbose_name="Отзыв")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class PartnerModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название партнера", blank=True, null=True)
    image = models.ImageField(upload_to="partners", verbose_name="Изображение партнера")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

class FooterModel(models.Model):
    phone = models.CharField(max_length=255, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    text = models.TextField(verbose_name="Текст")
    linkedin = models.CharField(max_length=255, verbose_name="Ссылка на linkedin", blank=True, null=True)
    facebook = models.CharField(max_length=255, verbose_name="Ссылка на facebook", blank=True, null=True)
    twitter = models.CharField(max_length=255, verbose_name="Ссылка на twitter", blank=True, null=True)

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"

    def save(self, *args, **kwargs):
        if not self.pk and FooterModel.objects.exists():
            raise ValidationError('Может быть только один объект Футер')
        return super(FooterModel, self).save(*args, **kwargs)
    
class ConsultModel(models.Model):
    image_1 = models.ImageField(upload_to="consult", verbose_name="Изображение 1")
    image_2 = models.ImageField(upload_to="consult", verbose_name="Изображение 2")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    link = models.CharField(max_length=255, verbose_name="Ссылка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"

    def save(self, *args, **kwargs):
        if not self.pk and ConsultModel.objects.exists():
            raise ValidationError('Может быть только один объект Консультация')
        return super(ConsultModel, self).save(*args, **kwargs)
    
class BlockModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    link = models.CharField(max_length=255, verbose_name="Ссылка")
    image = models.ImageField(upload_to="blocks", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"

    def save(self, *args, **kwargs):
        if not self.pk and BlockModel.objects.exists():
            raise ValidationError('Может быть только один объект Блок')
        return super(BlockModel, self).save(*args, **kwargs)