# Generated by Django 2.1 on 2020-01-20 18:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 20, 18, 20, 37, 288919, tzinfo=utc), verbose_name='Fecha de Publicación'),
        ),
    ]
