from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items

from fluentcms_file.models import FileItem


class FileTests(TestCase):
    """
    Testing file plugin
    """

    def test_output(self):
        """
        Test the standard file
        """
        item = create_content_item(FileItem, file=SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg"), name="file.jpg")
        self.assertHTMLEqual(
            render_content_items([item]).html,
            '<p class="file">'
            f'<a href="{item.file.url}">'
            '<span class="filename">'
            'file.jpg<span class="filesize">'
            '(12 bytes)'
            '</span>'
            '</span>'
            '</a>'
            "</p>",
        )
