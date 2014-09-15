# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20140907_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='theid',
            new_name='product_id',
        ),
    ]
