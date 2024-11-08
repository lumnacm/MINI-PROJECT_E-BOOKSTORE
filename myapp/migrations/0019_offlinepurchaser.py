# Generated by Django 5.1 on 2024-10-27 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_bill_details_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflinePurchaser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('number', models.BigIntegerField()),
                ('date', models.DateField()),
                ('place', models.TextField()),
                ('BOOK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.book')),
            ],
        ),
    ]
