# Generated by Django 5.0.6 on 2024-07-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='activity_status',
            field=models.BooleanField(default=True),
        ),
    ]
