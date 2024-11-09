# Generated by Django 5.1 on 2024-10-10 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_review_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='BILL_DETAILS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.bill_details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='BILL_DETAILS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.bill_details'),
            preserve_default=False,
        ),
    ]