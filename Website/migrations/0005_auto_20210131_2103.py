# Generated by Django 3.1.5 on 2021-01-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='correct_answer',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tests',
            name='explanation',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
