# Generated by Django 3.2.8 on 2022-07-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='src',
        ),
        migrations.AddField(
            model_name='photo',
            name='img',
            field=models.ImageField(blank=True, upload_to='photo/%Y%m%d/'),
        ),
    ]
