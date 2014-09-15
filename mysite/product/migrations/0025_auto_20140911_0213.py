# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20140907_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alcohol',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='product.Product')),
                ('alc_tags', models.CharField(default=b'vodka', max_length=50, choices=[(b'gin', b'Gin'), (b'vodka', b'Vodka'), (b'whiskey', b'Whiskey'), (b'special', b'Special')])),
            ],
            options={
            },
            bases=('product.product',),
        ),
        migrations.RemoveField(
            model_name='product',
            name='alcohol_tags',
        ),
    ]
