# Generated by Django 4.0.5 on 2022-06-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True, default='Please update your about..!!', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Please update your bio..!!', max_length=400, null=True),
        ),
    ]
