# Generated by Django 3.2.7 on 2021-09-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposaltitle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposetitle',
            name='status',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
