# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'',
        ensure_csrf_cookie(TemplateView.as_view(template_name='index.html')),
        name='index',
    ),
]
