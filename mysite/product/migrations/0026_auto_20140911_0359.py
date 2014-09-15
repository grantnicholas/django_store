# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from semantics3 import Products

from decimal import *

def import_shoes(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Shoe = apps.get_model("product", "Product")
    products = Products(api_key = "SEM383288C8F0304F7BB107E2E110B0420D3",api_secret = "MGYwZjgxZTVkOTVmZmY5OTEwYzlkMWI4MDAxMzk3YjA")
    products.products_field( "name", "Shoes" )
    products.products_field( "limit", 100 )
    results = products.get_products();
    resultarr = results['results'];
    count = 1;
    for i,var in enumerate(resultarr):
		s = Shoe(id = count, name= var['name'], price= Decimal(var['price']), stock= 1, description= var['category']);
		s.save()
		count=count+1;
	
	


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20140911_0213'),
    ]

    operations = [
		migrations.RunPython(import_shoes)
    ]
