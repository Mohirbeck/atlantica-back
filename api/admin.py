from django.contrib import admin
from .models import (
    NewsModel,
    ProjectModel,
    ProjectCategoryModel,
    ServiceModel,
    RequestModel,
    BannerModel,
    FooterModel,
    ReviewModel,
    ConsultModel,
    BlockModel,
    PartnerModel,
    AboutUsModel,
)
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

# Register your models here.

admin.site.site_header = "Atlantica Admin"
admin.site.site_title = "Atlantica Admin Portal"
admin.site.index_title = "Welcome to Atlantica Admin Portal"
# admin.site.unregister(Group)
# admin.site.unregister(User)


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at", "is_active")
    list_display_links = ("id", "title")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                    "short_description_ru",
                    "image",
                    "is_active",
                )
            },
        ),
        (
            _("English"),
            {"fields": ("title_en", "description_en", "short_description_en")},
        ),
        (
            _("Chinese"),
            {"fields": ("title_zh", "description_zh", "short_description_zh")},
        ),
    )


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "client",
        "date",
        "status",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_display_links = ("id", "name")
    list_filter = ("is_active", "status", "category")
    search_fields = ("name", "description", "client")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                    "description_ru",
                    "short_description_ru",
                    "client_ru",
                    "image",
                    "category",
                    "service",
                    "date",
                    "is_active",
                    "status",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                    "description_en",
                    "short_description_en",
                    "client_en",
                )
            },
        ),
        (
            _("Chinese"),
            {
                "fields": (
                    "name_zh",
                    "description_zh",
                    "short_description_zh",
                    "client_zh",
                )
            },
        ),
    )


@admin.register(ProjectCategoryModel)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_per_page = 25

    fieldsets = (
        (_("Russian"), {"fields": ("name_ru",)}),
        (_("English"), {"fields": ("name_en",)}),
        (_("Chinese"), {"fields": ("name_zh",)}),
    )


@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
        "is_active",
        "icon",
    )
    list_display_links = ("id", "name")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                    "description_ru",
                    "short_description_ru",
                    "icon",
                    "is_active",
                )
            },
        ),
        (
            _("English"),
            {"fields": ("name_en", "description_en", "short_description_en")},
        ),
        (
            _("Chinese"),
            {"fields": ("name_zh", "description_zh", "short_description_zh")},
        ),
    )


@admin.register(RequestModel)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email", "created_at", "updated_at")
    list_display_links = ("id", "name")
    search_fields = ("name", "phone", "email", "message")
    list_per_page = 25


@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_tag",
        "order",
        "created_at",
        "updated_at",
        "is_active",
    )
    list_display_links = (
        "id",
        "image_tag",
    )
    list_filter = ("is_active",)
    list_editable = ("order",)
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {"fields": ("image_ru", "link", "order", "is_active")},
        ),
        (_("English"), {"fields": ("image_en",)}),
        (_("Chinese"), {"fields": ("image_zh",)}),
    )

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="210px" height="90px">')


@admin.register(FooterModel)
class FooterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "email",
    )
    list_display_links = ("id",)
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "text_ru",
                    "phone",
                    "email",
                    "linkedin",
                    "facebook",
                    "twitter",
                )
            },
        ),
        (_("English"), {"fields": ("text_en",)}),
        (_("Chinese"), {"fields": ("text_zh",)}),
    )


@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "is_active")
    list_display_links = ("id", "name")
    list_filter = ("is_active",)
    search_fields = ("name", "description")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "name_ru",
                    "description_ru",
                    "position_ru",
                    "image",
                    "is_active",
                )
            },
        ),
        (
            _("English"),
            {
                "fields": (
                    "name_en",
                    "description_en",
                    "position_en",
                )
            },
        ),
        (
            _("Chinese"),
            {
                "fields": (
                    "name_zh",
                    "description_zh",
                    "position_zh",
                )
            },
        ),
    )


@admin.register(BlockModel)
class BlockAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                    "image",
                )
            },
        ),
        (_("English"), {"fields": ("title_en", "description_en")}),
        (_("Chinese"), {"fields": ("title_zh", "description_zh")}),
    )


@admin.register(ConsultModel)
class ConsultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                    "link",
                    "image_1",
                    "image_2",
                )
            },
        ),
        (_("English"), {"fields": ("title_en", "description_en")}),
        (_("Chinese"), {"fields": ("title_zh", "description_zh")}),
    )


@admin.register(PartnerModel)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "get_image",
        "name",
        "created_at",
        "updated_at",
    )
    list_display_links = (
        "get_image",
        "name",
    )
    search_fields = ("name",)
    list_per_page = 25

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="75px">')


@admin.register(AboutUsModel)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_per_page = 25

    fieldsets = (
        (
            _("Russian"),
            {
                "fields": (
                    "title_ru",
                    "description_ru",
                )
            },
        ),
        (_("English"), {"fields": ("title_en", "description_en")}),
        (_("Chinese"), {"fields": ("title_zh", "description_zh")}),
    )


# Path: api/serializers.py
