# Generated by Django 3.2.7 on 2021-09-27 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proposaltitle', '0003_auto_20210927_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titlecomment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
