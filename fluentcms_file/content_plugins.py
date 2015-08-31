# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import FileItem


@plugin_pool.register
class FilePlugin(ContentPlugin):
    """
    Plugin for rendering files.
    """
    model = FileItem
    category = _('Media')
    render_template = "fluentcms_file/file.html"
