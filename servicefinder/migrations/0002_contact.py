# Generated by Django 4.1.5 on 2023-04-10 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicefinder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('message', models.TextField()),
            ],
        ),
    ]
