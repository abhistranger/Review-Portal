# Generated by Django 3.0.4 on 2020-03-30 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0010_auto_20200330_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user_name',
        ),
    ]
