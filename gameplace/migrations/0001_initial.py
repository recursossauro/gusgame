# Generated by Django 3.0.7 on 2020-06-22 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='slug', max_length=200, verbose_name='Slug')),
                ('nickname', models.CharField(max_length=200, verbose_name='Nick')),
                ('avatar', models.ImageField(blank=True, max_length=500, null=True, upload_to='images/', verbose_name='Avatar')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Master',
                'verbose_name_plural': 'Masters',
                'unique_together': {('user', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, verbose_name='Nick')),
                ('avatar', models.ImageField(blank=True, max_length=500, null=True, upload_to='images/', verbose_name='Avatar')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplace.Master', verbose_name='Master')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Gamer',
                'verbose_name_plural': 'Gamers',
            },
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, verbose_name='Nick')),
                ('avatar', models.ImageField(blank=True, max_length=500, null=True, upload_to='images/', verbose_name='Avatar')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplace.Gamer', verbose_name='Masters')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Fan',
                'verbose_name_plural': 'Fans',
            },
        ),
    ]
