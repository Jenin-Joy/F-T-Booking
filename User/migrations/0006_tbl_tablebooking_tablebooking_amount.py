# Generated by Django 5.1.7 on 2025-03-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_tbl_bookedtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_tablebooking',
            name='tablebooking_amount',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
