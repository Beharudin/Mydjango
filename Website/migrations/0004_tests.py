# Generated by Django 3.1.5 on 2021-01-31 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_tutorials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=150)),
                ('subject_code', models.IntegerField()),
                ('year', models.IntegerField()),
                ('question', models.TextField(max_length=200)),
                ('choice_a', models.TextField(max_length=150)),
                ('choice_b', models.TextField(max_length=150)),
                ('choice_c', models.TextField(max_length=150)),
                ('choice_d', models.TextField(max_length=150)),
                ('paragraph', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
