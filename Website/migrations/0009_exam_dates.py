# Generated by Django 3.1.5 on 2021-02-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0008_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ec_day', models.IntegerField()),
                ('ec_month', models.IntegerField()),
                ('ec_year', models.IntegerField()),
                ('gc_day', models.IntegerField()),
                ('gc_month', models.IntegerField()),
                ('gc_year', models.IntegerField()),
                ('ec_date', models.DateField()),
                ('gc_date', models.DateField()),
            ],
        ),
    ]
