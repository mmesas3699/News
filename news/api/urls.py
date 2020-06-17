"""Greetings URL's."""

# Django
from django.urls import path

# Views
from api.views import ArticleView


urlpatterns = [
    path('v1/news/', ArticleView.as_view()),
]
