# Generated by Django 2.0.3 on 2018-04-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180325_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telephone',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]