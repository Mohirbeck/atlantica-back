from modeltranslation.translator import translator, TranslationOptions
from .models import (
    NewsModel,
    ProjectModel,
    ProjectCategoryModel,
    ServiceModel,
    FooterModel,
    ReviewModel,
    ConsultModel,
    BlockModel,
    BannerModel,
    AboutUsModel,
)


class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "description", "short_description")


class ProjectTranslationOptions(TranslationOptions):
    fields = ("name", "description", "client", "short_description")


class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description", "short_description")


class FooterTranslationOptions(TranslationOptions):
    fields = ("text",)


class ReviewTranslationOptions(TranslationOptions):
    fields = ("name", "position", "description")


class ConsultTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class BlockTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class BannerTranslationOptions(TranslationOptions):
    fields = ("image",)
    required_languages = ("ru", "en", "zh")


class AboutUsTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
    )
    required_languages = ("ru", "en", "zh")


translator.register(NewsModel, NewsTranslationOptions)
translator.register(ProjectModel, ProjectTranslationOptions)
translator.register(ProjectCategoryModel, ProjectCategoryTranslationOptions)
translator.register(ServiceModel, ServiceTranslationOptions)
translator.register(FooterModel, FooterTranslationOptions)
translator.register(ReviewModel, ReviewTranslationOptions)
translator.register(ConsultModel, ConsultTranslationOptions)
translator.register(BlockModel, BlockTranslationOptions)
translator.register(BannerModel, BannerTranslationOptions)
translator.register(AboutUsModel, AboutUsTranslationOptions)
