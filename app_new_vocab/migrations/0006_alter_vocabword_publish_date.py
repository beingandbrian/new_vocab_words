# Generated by Django 3.2 on 2021-04-27 19:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_new_vocab', '0005_alter_vocabword_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabword',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 27, 19, 10, 15, 379609, tzinfo=utc)),
        ),
    ]
