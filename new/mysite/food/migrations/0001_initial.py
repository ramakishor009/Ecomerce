# Generated by Django 4.2.11 on 2024-06-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=200)),
                ('itemdesc', models.CharField(max_length=200)),
                ('itemprice', models.IntegerField()),
            ],
        ),
    ]
