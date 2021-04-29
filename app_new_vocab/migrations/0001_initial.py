# Generated by Django 3.2 on 2021-04-27 18:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Brian', max_length=100)),
                ('last_name', models.CharField(default='Lyew', max_length=100)),
                ('full_name', models.CharField(default='Brian Lyew', max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='VocabWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_word', models.CharField(max_length=50)),
                ('definition', models.CharField(max_length=500)),
                ('sentence', models.CharField(max_length=500)),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocab_word', to='app_new_vocab.creator')),
            ],
        ),
    ]
