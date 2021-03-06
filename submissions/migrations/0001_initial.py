# Generated by Django 3.2.7 on 2022-01-05 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import submissions.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('submission_detail', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('duedate', models.DateTimeField()),
                ('status', models.IntegerField(default=0)),
                ('for_evaluation', models.BooleanField(default=False, null=True)),
                ('type_of_eval_grade', models.CharField(default='', max_length=50, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_content', models.TextField(blank=True, null=True)),
                ('pdf_submit', models.FileField(blank=True, max_length=500, null=True, upload_to='submissions/%Y-%m-%d/', validators=[submissions.validators.validate_file_extension])),
                ('filename', models.CharField(max_length=1000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='no submission', max_length=100)),
                ('for_eval_submit', models.BooleanField(default=False, null=True)),
                ('eval_grade_submit', models.CharField(max_length=100, null=True)),
                ('sub_evaluator', models.IntegerField(default=0, null=True)),
                ('if_seen', models.IntegerField(default=0, null=True)),
                ('submission_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='submissions.submissiontitle')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentSubmit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('submission_content', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='submissions.studentsubmit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
