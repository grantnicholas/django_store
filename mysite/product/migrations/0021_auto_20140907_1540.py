# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20140907_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alcohol_tags',
            field=models.CharField(default=b'SP', max_length=2, choices=[(b'GI', b'Gin'), (b'VO', b'Vodka'), (b'WH', b'Whiskey'), (b'SP', b'Special')]),
        ),
    ]
