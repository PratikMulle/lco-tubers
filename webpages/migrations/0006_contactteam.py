# Generated by Django 3.1.7 on 2021-03-08 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_auto_20210121_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=225)),
                ('phone', models.IntegerField(max_length=100)),
                ('email', models.CharField(max_length=225)),
                ('company_name', models.CharField(max_length=225)),
                ('subject', models.CharField(max_length=225)),
                ('message', models.CharField(max_length=225)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]