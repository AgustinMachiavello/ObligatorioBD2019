# Generated by Django 2.2.6 on 2019-10-31 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='end_point',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_point',
        ),
        migrations.AddField(
            model_name='route',
            name='end_point_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='route',
            name='end_point_lon',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='route',
            name='start_point_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='route',
            name='start_point_lon',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='route',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.Route')),
            ],
        ),
    ]