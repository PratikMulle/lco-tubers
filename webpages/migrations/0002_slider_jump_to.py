# Generated by Django 3.1.5 on 2021-01-21 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='jump_to',
            field=models.URLField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]