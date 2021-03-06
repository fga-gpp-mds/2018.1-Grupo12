# Generated by Django 2.0.3 on 2018-05-30 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20180528_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentrequest',
            name='doctor',
            field=models.ForeignKey(blank=True, help_text='Preferred doctor. It is not guaranteed that the appointment will be scheduled with the doctor preferred.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='users.HealthTeam', verbose_name='Doctor'),
        ),
    ]
