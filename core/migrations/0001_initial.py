# Generated by Django 4.1.2 on 2022-10-31 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=3000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('photoUrl', models.ImageField(blank=True, null=True, upload_to='csv_files', verbose_name='CSV File')),
                ('displayName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('aboutMe', models.CharField(max_length=300, null=True)),
                ('isWorker', models.IntegerField(blank=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['date_updated'],
            },
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='core.member')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postCommentText', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='core.member')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postText', models.TextField(blank=True, null=True)),
                ('postContentUrl', models.FileField(blank=True, null=True, upload_to='csv_files', verbose_name='CSV File')),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='core.member')),
                ('post_comments', models.ManyToManyField(blank=True, null=True, related_name='postComments', to='core.postcomment')),
                ('post_likes', models.ManyToManyField(blank=True, null=True, related_name='postLikes', to='core.postlike')),
            ],
        ),
    ]
