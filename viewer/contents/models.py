# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from ..users.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class UploadedFile(models.Model):
    file_name = models.CharField(max_length=120, null=False)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    file_content = models.FileField(upload_to='contents-files', null=False)
    user = models.ForeignKey(User, null=False)
    thumbnail = models.FileField(upload_to='contents-thumbnails', null=False)

    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.file_name)

        super(UploadedFile, self).save(*args, **kwargs)

