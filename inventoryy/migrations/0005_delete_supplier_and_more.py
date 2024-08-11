# Generated by Django 5.0.6 on 2024-07-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryy', '0004_supplier_alter_inventoryitem_minimum_stock_level_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='minimum_stock_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
