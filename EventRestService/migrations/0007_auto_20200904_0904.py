# Generated by Django 2.1 on 2020-09-04 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventRestService', '0006_auto_20200904_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='purpose',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
