# Generated by Django 3.0.1 on 2020-01-31 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0002_recordes_recorde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordes',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
