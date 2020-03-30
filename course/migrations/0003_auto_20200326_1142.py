# Generated by Django 3.0.4 on 2020-03-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200326_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_credit',
            field=models.CharField(default='Not Available', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_detail',
            field=models.CharField(default='Not Available', max_length=5000),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_name',
            field=models.CharField(default='Not Available', max_length=250),
        ),
    ]
