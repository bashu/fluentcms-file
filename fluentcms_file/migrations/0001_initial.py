# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('file', models.FileField(upload_to=b'', verbose_name='file')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='name', blank=True)),
            ],
            options={
                'db_table': 'contentitem_fluentcms_file_fileitem',
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
