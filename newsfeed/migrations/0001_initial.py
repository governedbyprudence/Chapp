# Generated by Django 3.2.4 on 2021-06-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=-1)),
                ('username', models.CharField(max_length=20)),
                ('liked_username', models.CharField(max_length=20)),
                ('img_id', models.IntegerField(default=-1)),
                ('comment', models.CharField(max_length=300)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='feed_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=-1)),
                ('username', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='newsfeed/images')),
                ('caption', models.CharField(max_length=300)),
                ('likes', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=-1)),
                ('username', models.CharField(max_length=20)),
                ('liked_username', models.CharField(max_length=20)),
                ('img_id', models.IntegerField(default=-1)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
