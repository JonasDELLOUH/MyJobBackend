# Generated by Django 4.1.2 on 2022-10-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_comments',
            new_name='postcomments',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_likes',
            new_name='postlikes',
        ),
    ]
