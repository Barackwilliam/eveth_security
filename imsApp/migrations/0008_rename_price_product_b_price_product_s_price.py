# Generated by Django 4.0.3 on 2025-02-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imsApp', '0007_invoice_date_created_invoice_date_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='b_price',
        ),
        migrations.AddField(
            model_name='product',
            name='s_price',
            field=models.FloatField(default=0),
        ),
    ]
