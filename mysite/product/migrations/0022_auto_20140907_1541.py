# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_auto_20140907_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alcohol_tags',
            field=models.CharField(default=b'special', max_length=2, choices=[(b'gin', b'Gin'), (b'vodka', b'Vodka'), (b'whiskey', b'Whiskey'), (b'special', b'Special')]),
        ),
    ]
