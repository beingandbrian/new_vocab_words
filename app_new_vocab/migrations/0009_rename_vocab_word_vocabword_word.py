# Generated by Django 3.2 on 2021-04-29 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_new_vocab', '0008_alter_vocabword_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vocabword',
            old_name='vocab_word',
            new_name='word',
        ),
    ]
