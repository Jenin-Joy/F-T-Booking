# Generated by Django 5.1.3 on 2025-01-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_tbl_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(max_length=30)),
                ('table_count', models.IntegerField(max_length=30)),
            ],
        ),
    ]
