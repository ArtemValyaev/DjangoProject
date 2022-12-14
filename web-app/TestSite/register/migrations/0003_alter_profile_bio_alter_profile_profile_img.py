# Generated by Django 4.1 on 2022-09-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=1000, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='static/main/images/profile-photo.png', upload_to='images/profile_img'),
        ),
    ]
