# Generated by Django 5.1.3 on 2024-12-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_alter_tbl_job_job_postdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_job',
            name='job_postdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
