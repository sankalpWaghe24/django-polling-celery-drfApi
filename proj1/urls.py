from polls.views import PollViewSet, ChoiceViewSet
from django.contrib import admin
from django.urls import path, include
from polls import views
from django.urls import re_path as url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"poll", PollViewSet, basename="poll")
router.register(r"choice", ChoiceViewSet, basename="choice")
urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("polls/", include("polls.urls", namespace="polls")),
    url(r"^api/polls/", include(router.urls)),
]
