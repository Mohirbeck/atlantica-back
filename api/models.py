from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


def validate_file_extension(value):
    if not value.name.endswith(".svg"):
        raise ValidationError(_("Только SVG файлы"))


class ServiceModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название услуги"))
    description = RichTextUploadingField(
        verbose_name=_("Описание услуги"), blank=True, null=True
    )
    short_description = models.TextField(
        null=True, blank=True, default="", verbose_name=_("Краткое описание")
    )
    icon = models.FileField(
        upload_to="services",
        verbose_name=_("Иконка услуги"),
        blank=True,
        null=True,
        help_text="Рекомендуемый размер 64x64",
        validators=[validate_file_extension],
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))

    def __str__(self):
        return self.name

    @property
    def get_projects(self):
        return ProjectModel.objects.filter(is_active=True, service=self.id).order_by(
            "-created_at"
        )[:7]

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")


class ProjectModel(models.Model):
    statuses = (
        ("В работе", "В работе"),
        ("Завершен", "Завершен"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Название проекта"))
    description = RichTextUploadingField(
        verbose_name=_("Описание проекта"), blank=True, null=True
    )
    short_description = models.TextField(
        null=True, blank=True, default="", verbose_name=_("Краткое описание")
    )
    image = models.ImageField(
        upload_to="projects",
        verbose_name=_("Изображение проекта"),
        blank=True,
        null=True,
    )
    client = models.CharField(
        max_length=255, verbose_name=_("Клиент"), blank=True, null=True
    )
    category = models.ForeignKey(
        "ProjectCategoryModel",
        on_delete=models.CASCADE,
        verbose_name=_("Категория"),
        blank=True,
        null=True,
    )
    service = models.ManyToManyField(
        "ServiceModel", verbose_name=_("Услуга"), blank=True
    )
    date = models.DateField(verbose_name=_("Дата"), blank=True, null=True)
    status = models.CharField(
        max_length=255,
        choices=statuses,
        verbose_name=_("Статус"),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))

    def __str__(self):
        return self.name

    @property
    def get_similar_projects(self):
        return (
            ProjectModel.objects.filter(is_active=True, category=self.category)
            .exclude(id=self.id)
            .order_by("-created_at")[:7]
        )

    class Meta:
        verbose_name = _("Проект")
        verbose_name_plural = _("Проекты")


class ProjectCategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название категории"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Категория проекта")
        verbose_name_plural = _("Категории проектов")


class NewsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    description = RichTextUploadingField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    short_description = models.TextField(
        null=True, blank=True, default="", verbose_name=_("Краткое описание")
    )
    image = models.ImageField(
        upload_to="news", verbose_name=_("Изображение"), blank=True, null=True
    )
    views = models.BigIntegerField(verbose_name=_("Просмотры"), default=0)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))

    def __str__(self):
        return self.title

    @property
    def get_latest_news(self):
        return (
            NewsModel.objects.filter(is_active=True)
            .exclude(id=self.id)
            .order_by("-created_at")[:5]
        )

    @property
    def get_popular_news(self):
        return (
            NewsModel.objects.filter(is_active=True)
            .exclude(id=self.id)
            .order_by("-views")[:5]
        )

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")


class RequestModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=255, verbose_name=_("Телефон"))
    message = models.TextField(verbose_name=_("Сообщение"), blank=True, null=True)
    type = models.CharField(max_length=255, verbose_name=_("Тип"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")


class BannerModel(models.Model):
    link = models.CharField(
        max_length=255, verbose_name=_("Ссылка"), blank=True, null=True
    )
    image = models.ImageField(upload_to="banners", verbose_name=_("Изображение"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))
    order = models.IntegerField(verbose_name=_("Порядок"), default=0)

    def __str__(self):
        return "Баннер"

    class Meta:
        verbose_name = _("Баннер")
        verbose_name_plural = _("Баннеры")


class ReviewModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    position = models.CharField(max_length=255, verbose_name=_("Должность"))
    image = models.ImageField(upload_to="reviews", verbose_name=_("Изображение"))
    description = models.TextField(verbose_name=_("Отзыв"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")


class PartnerModel(models.Model):
    name = models.CharField(
        max_length=255, verbose_name=_("Название партнера"), blank=True, null=True
    )
    image = models.ImageField(
        upload_to="partners", verbose_name=_("Изображение партнера")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))
    is_active = models.BooleanField(default=True, verbose_name=_("Активность"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Партнер")
        verbose_name_plural = _("Партнеры")


class FooterModel(models.Model):
    phone = models.CharField(max_length=255, verbose_name=_("Телефон"))
    email = models.EmailField(verbose_name=_("Email"))
    text = models.TextField(verbose_name=_("Текст"))
    linkedin = models.CharField(
        max_length=255, verbose_name=_("Ссылка на linkedin"), blank=True, null=True
    )
    facebook = models.CharField(
        max_length=255, verbose_name=_("Ссылка на facebook"), blank=True, null=True
    )
    twitter = models.CharField(
        max_length=255, verbose_name=_("Ссылка на twitter"), blank=True, null=True
    )

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _("Футер")
        verbose_name_plural = _("Футер")

    def save(self, *args, **kwargs):
        if not self.pk and FooterModel.objects.exists():
            raise ValidationError(_("Может быть только один объект Футер"))
        return super(FooterModel, self).save(*args, **kwargs)


class ConsultModel(models.Model):
    image_1 = models.ImageField(upload_to="consult", verbose_name=_("Изображение 1"))
    image_2 = models.ImageField(upload_to="consult", verbose_name=_("Изображение 2"))
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    description = models.TextField(verbose_name=_("Описание"))
    link = models.CharField(max_length=255, verbose_name=_("Ссылка"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Консультация")
        verbose_name_plural = _("Консультации")

    def save(self, *args, **kwargs):
        if not self.pk and ConsultModel.objects.exists():
            raise ValidationError(_("Может быть только один объект Консультация"))
        return super(ConsultModel, self).save(*args, **kwargs)


class BlockModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    description = models.TextField(verbose_name=_("Описание"))
    link = models.CharField(max_length=255, verbose_name=_("Ссылка"))
    image = models.ImageField(upload_to="blocks", verbose_name=_("Изображение"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Блок")
        verbose_name_plural = _("Блоки")

    def save(self, *args, **kwargs):
        if not self.pk and BlockModel.objects.exists():
            raise ValidationError(_("Может быть только один объект Блок"))
        return super(BlockModel, self).save(*args, **kwargs)


class AboutUsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    description = RichTextUploadingField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Дата создания")
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("О нас")
        verbose_name_plural = _("О нас")

    def save(self, *args, **kwargs):
        if not self.pk and AboutUsModel.objects.exists():
            raise ValidationError(_("Может быть только один объект О нас"))
        return super(AboutUsModel, self).save(*args, **kwargs)
