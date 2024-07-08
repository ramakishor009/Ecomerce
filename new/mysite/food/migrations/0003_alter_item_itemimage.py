# Generated by Django 4.2.11 on 2024-06-06 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemimage',
            field=models.CharField(default='data:image/jpeg;base64,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', max_length=500),
        ),
    ]
