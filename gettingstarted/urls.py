from django.contrib import admin
from django.urls import path, include


import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    # Uncomment this and the entry in `INSTALLED_APPS` if you wish to use the Django admin feature:
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
    path("admin/", admin.site.urls),
    path("hello/", include("hello.urls")),
]
