# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import UploadedFile


@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'slug']
    search_fields = ['file_name', 'slug']
