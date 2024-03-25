from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('bbs/', include('bbs.urls')),
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('', RedirectView.as_view(url='/bbs/')),
]
