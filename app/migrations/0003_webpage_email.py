# Generated by Django 5.1.3 on 2024-12-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_topic_name_accessrecords_webpage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='mayank@email.com', max_length=254),
        ),
    ]
