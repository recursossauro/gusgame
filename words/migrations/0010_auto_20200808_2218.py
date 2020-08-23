# Generated by Django 3.0.7 on 2020-08-09 01:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameplace', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0009_auto_20200808_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='right',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplace.Gamer', verbose_name='Gamer'),
        ),
        migrations.AlterUniqueTogether(
            name='right',
            unique_together={('user', 'gamer', 'word')},
        ),
    ]
