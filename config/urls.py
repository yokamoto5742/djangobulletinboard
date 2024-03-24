from django.contrib import admin
from django.urls import path, include


import hello.views

urlpatterns = [
    path("bbs/", include("bbs.urls")),
    path("admin/", admin.site.urls),
    path("hello/", include("hello.urls")),
]
