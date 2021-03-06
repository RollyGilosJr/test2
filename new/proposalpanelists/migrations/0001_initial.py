# Generated by Django 3.2.7 on 2021-09-29 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proposaltitle', '0004_alter_titlecomment_author'),
        ('register', '0003_alter_userprofile_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdviserAndPanelist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('adviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adviser', to='register.userprofile')),
                ('panel1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panel1', to='register.userprofile')),
                ('panel2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panel2', to='register.userprofile')),
                ('panel3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panel3', to='register.userprofile')),
                ('panel4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panel4', to='register.userprofile')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proposaltitle.proposetitle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
