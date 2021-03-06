# Generated by Django 3.2.7 on 2022-01-05 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulerEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduler_event', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SchedulerDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_event', models.DateField(max_length=1000)),
                ('event_d', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_d', to='evaluation.schedulerevent')),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('adv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adv', to=settings.AUTH_USER_MODEL)),
                ('date', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date', to='evaluation.schedulerdate')),
                ('event', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='evaluation.schedulerevent')),
                ('proponents', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proponents', to='register.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
