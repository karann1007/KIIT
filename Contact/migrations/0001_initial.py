# Generated by Django 2.1 on 2021-04-11 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Local',
            fields=[
                ('comp_lcl_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_no', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('ho', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scheduler.Company_Details')),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scheduler.Office_Types')),
            ],
        ),
    ]
