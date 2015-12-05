# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UploadedFileList.as_view(),
        name='list'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<slug>[\w.@+-]+)/$',
        view=views.UploadedFileDetail.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UploadedFileUpdate.as_view(),
        name='update'
    ),
]
