# Generated by Django 3.2.8 on 2022-07-06 05:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('src', models.CharField(max_length=200)),
                ('cap', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
