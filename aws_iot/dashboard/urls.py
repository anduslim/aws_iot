# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [

    # URL pattern for the DashboardRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.DashboardRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the DashboardMainView
    url(
        regex=r'^dashboard/$',
        view=views.DashboardMainView.as_view(),
        name='dashboard'
    ),

    # URL pattern for the DashboardManageView
    url(
        regex=r'^manage/$',
        view=views.DashboardManageView.as_view(),
        name='manage'
    ),

    # URL pattern for the DashboardManageView
    url(
        regex=r'^user/$',
        view=views.DashboardUserView.as_view(),
        name='user'
    ),
]
