# Generated by Django 2.1 on 2021-04-22 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Scheduler', '0003_auto_20210421_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_alumini',
            name='comp_lcl_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Contact.Company_Local'),
        ),
    ]