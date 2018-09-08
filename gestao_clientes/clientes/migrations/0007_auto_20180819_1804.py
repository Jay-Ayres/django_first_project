# Generated by Django 2.1 on 2018-08-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_remove_pessoa_idade'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(default=0, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='teste',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]