# Generated by Django 3.2 on 2021-04-27 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_new_vocab', '0007_alter_vocabword_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabword',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vocab_word', to='app_new_vocab.creator'),
        ),
    ]