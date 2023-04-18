from rest_framework import serializers
from .models import (
    NewsModel,
    ProjectModel,
    ProjectCategoryModel,
    ServiceModel,
    RequestModel,
    BannerModel,
    BlockModel,
    ReviewModel,
    ConsultModel,
    FooterModel,
    PartnerModel,
)
from bs4 import BeautifulSoup


class NewsListSerializer(serializers.ModelSerializer):
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()
    description_uz = serializers.SerializerMethodField()

    def get_description_ru(self, obj):
        if obj.description_ru is None or obj.description_ru == "":
            return ""
        soup = BeautifulSoup(obj.description_ru, "html.parser")
        if soup is None:
            return ""
        else:
            return soup.text[:100]

    def get_description_en(self, obj):
        if obj.description_en is None or obj.description_en == "":
            return ""
        soup = BeautifulSoup(obj.description_en, "html.parser")
        if soup is None:
            return ""
        else:
            return soup.text[:100]

    def get_description_uz(self, obj):
        if obj.description_uz is None or obj.description_uz == "":
            return ""
        soup = BeautifulSoup(obj.description_uz, "html.parser")
        if soup is None:
            return ""
        else:
            return soup.text[:100]

    class Meta:
        model = NewsModel
        exclude = (
            "is_active",
            "description",
            "title",
        )


class NewsSerializer(serializers.ModelSerializer):
    latest_news = NewsListSerializer(many=True, read_only=True, source="get_latest_news")
    popular_news = NewsListSerializer(many=True, read_only=True, source="get_popular_news")

    class Meta:
        model = NewsModel
        exclude = (
            "is_active",
            "description",
            "title",
        )


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategoryModel
        fields = "__all__"


class ProjectListSerializer(serializers.ModelSerializer):
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()
    description_uz = serializers.SerializerMethodField()

    def get_description_ru(self, obj):
        if obj.description_ru is None or obj.description_ru == "":
            return ""
        soup = BeautifulSoup(obj.description_ru, "html.parser")
        if soup.text is None or soup.text == "":
            return ""
        else:
            return soup.text[:100]

    def get_description_en(self, obj):
        if obj.description_en is None or obj.description_en == "":
            return ""
        soup = BeautifulSoup(obj.description_en, "html.parser")
        if soup.text is None or soup.text == "":
            return ""
        else:
            return soup.text[:100]

    def get_description_uz(self, obj):
        if obj.description_uz is None or obj.description_uz == "":
            return ""
        soup = BeautifulSoup(obj.description_uz, "html.parser")
        if soup.text is None or soup.text == "":
            return ""
        else:
            return soup.text[:100]

    class Meta:
        model = ProjectModel
        exclude = (
            "is_active",
            "description",
            "name",
            "service",
            "category",
            "status",
            "date",
            "client",
            "client_ru",
            "client_en",
            "client_uz",
        )


class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(many=False, read_only=True)
    similar_projects = serializers.SerializerMethodField()

    def get_similar_projects(self, obj):
        projects = (
            ProjectModel.objects.filter(is_active=True, category=obj.category)
            .exclude(id=obj.id)
            .order_by("-created_at")[:7]
        )
        return ProjectListSerializer(projects, many=True).data

    class Meta:
        model = ProjectModel
        exclude = ("is_active",)


class ServiceListSerializer(serializers.ModelSerializer):
    description_ru = serializers.SerializerMethodField()
    description_en = serializers.SerializerMethodField()
    description_uz = serializers.SerializerMethodField()

    def get_description_ru(self, obj):
        if obj.description_ru is None or obj.description_ru == "":
            return ""
        soup = BeautifulSoup(obj.description_ru, "html.parser")
        if soup is None:
            return ""
        else:
            return soup.text[:100]

    def get_description_en(self, obj):
        if obj.description_en is None or obj.description_en == "":
            return ""
        soup = BeautifulSoup(obj.description_en, "html.parser")
        if soup is None:
            return ""
        else:
            return soup.text[:100]

    def get_description_uz(self, obj):
        if obj.description_uz is None or obj.description_uz == "":
            return ""
        soup = BeautifulSoup(obj.description_uz, "html.parser")
        if soup is None:
            return ""
        else:
            return soup.text[:100]

    class Meta:
        model = ServiceModel
        exclude = (
            "is_active",
            "name",
            "description",
        )


class ServiceSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()

    def get_projects(self, obj):
        return ProjectListSerializer(
            ProjectModel.objects.filter(is_active=True, service=obj).order_by(
                "-created_at"
            )[:7],
            many=True,
        ).data

    class Meta:
        model = ServiceModel
        exclude = ("is_active",)


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestModel
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        exclude = ("is_active",)


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockModel
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        exclude = ("is_active",)


class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultModel
        fields = "__all__"


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerModel
        exclude = ("is_active",)
