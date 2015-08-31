# -*- coding: utf-8 -*-

import os

from future.builtins import str
from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from fluent_contents.models.db import ContentItem

from . import appsettings 


@python_2_unicode_compatible
class FileItem(ContentItem):

    file = models.FileField(_("file"), upload_to=appsettings.FLUENTCMS_FILE_UPLOAD_TO)
    name = models.CharField(_("name"), max_length=255, null=True, blank=True)

    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )), default='')

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")

    def __str__(self):
        if self.name:
            return self.name
        elif self.file:
            return str(os.path.basename(self.file.name))
        return "<empty>"
