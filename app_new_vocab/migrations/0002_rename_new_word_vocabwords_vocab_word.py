# Generated by Django 3.2 on 2021-04-27 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_new_vocab', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocabwords',
            old_name='new_word',
            new_name='vocab_word',
        ),
    ]