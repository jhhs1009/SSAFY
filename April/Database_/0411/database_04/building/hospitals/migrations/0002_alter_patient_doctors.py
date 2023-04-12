# Generated by Django 3.2.12 on 2023-04-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(related_name='patients', to='hospitals.Doctor'),
        ),
    ]
