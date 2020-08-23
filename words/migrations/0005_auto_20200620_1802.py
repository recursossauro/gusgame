# Generated by Django 3.0.7 on 2020-06-20 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0004_auto_20200618_2124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fan',
            options={'verbose_name': 'Fan', 'verbose_name_plural': 'Fans'},
        ),
        migrations.AlterModelOptions(
            name='gamer',
            options={'verbose_name': 'Gamer', 'verbose_name_plural': 'Gamers'},
        ),
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'Master', 'verbose_name_plural': 'Masters'},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'verbose_name': 'Word', 'verbose_name_plural': 'Word'},
        ),
        migrations.AddField(
            model_name='master',
            name='slug',
            field=models.SlugField(default='slug', max_length=200, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.Gamer', verbose_name='Masters'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='fan',
            name='nickname',
            field=models.CharField(max_length=200, verbose_name='Nick'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.Master', verbose_name='Master'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='nickname',
            field=models.CharField(max_length=200, verbose_name='Nick'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='master',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='master',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='master',
            name='nickname',
            field=models.CharField(max_length=200, verbose_name='Nick'),
        ),
        migrations.AlterField(
            model_name='word',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='word',
            name='gamer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='words.Gamer', verbose_name='Masters'),
        ),
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.ImageField(blank=True, max_length=500, null=True, upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='word',
            name='master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='words.Master', verbose_name='Masters'),
        ),
        migrations.AlterField(
            model_name='word',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=200, verbose_name='Word'),
        ),
        migrations.AlterUniqueTogether(
            name='master',
            unique_together={('user', 'slug')},
        ),
    ]
