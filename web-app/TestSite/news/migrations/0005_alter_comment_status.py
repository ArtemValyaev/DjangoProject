# Generated by Django 4.1 on 2022-09-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('HIDDEN', 'hidden'), ('SHOW', 'show')], default='hidden', max_length=7, verbose_name=''),
        ),
    ]
