# Generated by Django 5.1.3 on 2025-01-02 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_tbl_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_table',
            name='table_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tbl_table',
            name='table_number',
            field=models.IntegerField(),
        ),
    ]
