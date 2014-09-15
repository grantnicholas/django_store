# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20140911_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='product.Product')),
                ('shoe_tags', models.CharField(default=b'none', max_length=50, null=True, blank=True, choices=[(b'running', b'Running'), (b'orthotic', b'Orthotic'), (b'diabetic', b'Diabetic'), (b'none', b'None')])),
            ],
            options={
            },
            bases=('product.product',),
        ),
    ]
