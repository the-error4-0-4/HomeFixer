# Generated by Django 4.1.5 on 2023-04-13 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicefinder', '0011_partnerprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerService',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('service', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=40)),
                ('timing', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('userstatus', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicefinder.partnerprofile')),
            ],
        ),
    ]