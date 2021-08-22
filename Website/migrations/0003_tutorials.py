# Generated by Django 3.1.5 on 2021-01-31 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_auto_20210131_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_video', models.FileField(upload_to='')),
                ('lecture_name', models.CharField(max_length=150)),
                ('lecture_subject', models.CharField(max_length=150)),
                ('teacher_name', models.CharField(max_length=150)),
            ],
        ),
    ]
