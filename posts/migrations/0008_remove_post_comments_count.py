# Generated by Django 3.0.2 on 2020-02-27 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_comments_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments_count',
        ),
    ]
