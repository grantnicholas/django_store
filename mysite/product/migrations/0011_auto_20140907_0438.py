# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20140907_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'media/no-img.png', upload_to=b'media/', null=True, verbose_name=b'Image', blank=True),
        ),
    ]
