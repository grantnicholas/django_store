# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20140907_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'./no-img.png', upload_to=b'./static', null=True, verbose_name=b'Image', blank=True),
        ),
    ]
