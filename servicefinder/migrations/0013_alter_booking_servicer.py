# Generated by Django 4.1.5 on 2023-04-13 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicefinder', '0012_partnerservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='servicer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicefinder.partnerservice'),
        ),
    ]
