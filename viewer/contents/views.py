# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, UpdateView
from .models import UploadedFile

from braces.views import LoginRequiredMixin


class UploadedFileDetail(LoginRequiredMixin, DetailView):
    model = UploadedFile
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class UploadedFileUpdate(LoginRequiredMixin, UpdateView):
    model = UploadedFile
    fields = ['file_name', ]

    # send the user back to the detail page after a successful update
    def get_success_url(self):
        return reverse("contents:detail",
                       kwargs={"slug": self.object.slug})


class UploadedFileList(LoginRequiredMixin, ListView):
    model = UploadedFile
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
