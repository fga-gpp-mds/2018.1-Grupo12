# Generated by Django 2.0.3 on 2018-04-05 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import drdown.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180404_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(help_text='Please, use enter a valid CPF in the following format: XXX.XXX.XXX-XX', max_length=14, unique=True, validators=[drdown.utils.validators.validate_cpf])),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Patient')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]