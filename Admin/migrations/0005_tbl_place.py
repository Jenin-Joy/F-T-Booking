# Generated by Django 5.1.3 on 2024-12-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_rename_tbl_admin_tbl_adminreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=30)),
            ],
        ),
    ]
