# Generated by Django 5.1 on 2024-10-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_bill_details_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill_details',
            name='reason',
            field=models.CharField(default='pending', max_length=500),
        ),
    ]