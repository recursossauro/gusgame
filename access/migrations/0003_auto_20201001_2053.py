# Generated by Django 3.0.7 on 2020-10-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_auto_20200622_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, default='/static/images/generic-avatar.png', max_length=500, null=True, upload_to='images/', verbose_name='Photo'),
        ),
    ]
