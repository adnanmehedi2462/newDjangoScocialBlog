# Generated by Django 4.0.5 on 2022-06-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=1, upload_to='postimage/'),
            preserve_default=False,
        ),
    ]