# Generated by Django 3.2.9 on 2021-12-03 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebSite', '0002_auto_20211203_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
