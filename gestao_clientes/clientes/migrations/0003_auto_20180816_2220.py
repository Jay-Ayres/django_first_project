# Generated by Django 2.1 on 2018-08-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20180816_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='teste',
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]