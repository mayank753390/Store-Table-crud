# Generated by Django 5.1.3 on 2024-12-25 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecords',
            old_name='Topic_name',
            new_name='webpage',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='Topic_name',
            new_name='topic_name',
        ),
        migrations.RenameField(
            model_name='webpage',
            old_name='Topic_name',
            new_name='topic',
        ),
    ]
