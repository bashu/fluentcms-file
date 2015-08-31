# -*- coding: utf-8 -*-

from django.conf import settings

FLUENTCMS_FILE_UPLOAD_TO = getattr(settings, 'FLUENTCMS_FILE_UPLOAD_TO', '.')
