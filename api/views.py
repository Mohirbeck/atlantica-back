from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (
    NewsModel,
    ProjectModel,
    ServiceModel,
    RequestModel,
    BannerModel,
    BlockModel,
    ReviewModel,
    ConsultModel,
    FooterModel,
    PartnerModel,
)
from .serializers import (
    NewsSerializer,
    NewsListSerializer,
    ProjectSerializer,
    ProjectListSerializer,
    ServiceSerializer,
    ServiceListSerializer,
    RequestSerializer,
    BannerSerializer,
    BlockSerializer,
    ReviewSerializer,
    ConsultSerializer,
    FooterSerializer,
    PartnerSerializer,
)
from rest_framework.pagination import LimitOffsetPagination


class DefaultPagination(LimitOffsetPagination):
    default_limit = 12
    max_limit = 100


class NewsListAPIView(ListAPIView):
    queryset = NewsModel.objects.filter(is_active=True)
    serializer_class = NewsListSerializer
    pagination_class = DefaultPagination


class NewsDetailAPIView(RetrieveAPIView):
    queryset = NewsModel.objects.filter(is_active=True)
    serializer_class = NewsSerializer

@api_view(["POST"])
def news_view_count(request, pk):
    news = NewsModel.objects.get(pk=pk)
    news.views += 1
    news.save()
    return Response({"views": news.views})

class ProjectListAPIView(ListAPIView):
    queryset = ProjectModel.objects.filter(is_active=True)
    serializer_class = ProjectListSerializer
    pagination_class = DefaultPagination


class ProjectDetailAPIView(RetrieveAPIView):
    queryset = ProjectModel.objects.filter(is_active=True)
    serializer_class = ProjectSerializer


class ServiceListAPIView(ListAPIView):
    queryset = ServiceModel.objects.filter(is_active=True)
    serializer_class = ServiceListSerializer
    pagination_class = DefaultPagination


class ServiceDetailAPIView(RetrieveAPIView):
    queryset = ServiceModel.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class RequestCreateAPIView(CreateAPIView):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer


class BannerListAPIView(ListAPIView):
    queryset = BannerModel.objects.filter(is_active=True).order_by("order")
    serializer_class = BannerSerializer

class BlockListAPIView(ListAPIView):
    queryset = BlockModel.objects.all()
    serializer_class = BlockSerializer

class ReviewListAPIView(ListAPIView):
    queryset = ReviewModel.objects.filter(is_active=True)
    serializer_class = ReviewSerializer

class ConsultListAPIView(ListAPIView):
    queryset = ConsultModel.objects.all()
    serializer_class = ConsultSerializer

class FooterListAPIView(ListAPIView):
    queryset = FooterModel.objects.all()
    serializer_class = FooterSerializer

class PartnerListAPIView(ListAPIView):
    queryset = PartnerModel.objects.filter(is_active=True)
    serializer_class = PartnerSerializer


# Compare this snippet from api/urls.py:
