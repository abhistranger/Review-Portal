# Generated by Django 3.0.4 on 2020-03-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0008_reviews_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='user',
        ),
        migrations.AddField(
            model_name='reviews',
            name='user_name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
