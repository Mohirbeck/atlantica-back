from . import views
from django.urls import path

urlpatterns = [
    path("news/", views.NewsListAPIView.as_view()),
    path("news/<int:pk>/", views.NewsDetailAPIView.as_view()),
    path("news/<int:pk>/views", views.news_view_count, name="news_view_count"),
    path("projects/", views.ProjectListAPIView.as_view()),
    path("projects/<int:pk>/", views.ProjectDetailAPIView.as_view()),
    path("services/", views.ServiceListAPIView.as_view()),
    path("services/<int:pk>/", views.ServiceDetailAPIView.as_view()),
    path("request/", views.RequestCreateAPIView.as_view()),
    path("banner/", views.BannerListAPIView.as_view()),
    path("block/", views.BlockListAPIView.as_view()),
    path("review/", views.ReviewListAPIView.as_view()),
    path("consult/", views.ConsultListAPIView.as_view()),
    path("footer/", views.FooterListAPIView.as_view()),
    path('partners/', views.PartnerListAPIView.as_view()),
    path('about/', views.AboutUsAPIView.as_view()),
]