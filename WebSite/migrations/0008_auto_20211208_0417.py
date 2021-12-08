# Generated by Django 3.2.9 on 2021-12-08 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebSite', '0007_auto_20211208_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='review',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
