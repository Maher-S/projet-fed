from django.urls import path
from .views import HomePageView


urlpatterns = [
    path("", HomePageView.as_view(), name='home'), # homepage
    #path("", views.article_list, name='article_list'),
]