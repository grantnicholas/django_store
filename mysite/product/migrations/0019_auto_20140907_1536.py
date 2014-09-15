# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_alcohol_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alcohol_tags',
            field=models.CharField(default=b'Special', max_length=100, choices=[(b'Gin', b'Gin'), (b'Vodka', b'Vodka'), (b'Whiskey', b'Whiskey'), (b'Special', b'Special')]),
        ),
    ]
