# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='home/about.html'), name="about"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
