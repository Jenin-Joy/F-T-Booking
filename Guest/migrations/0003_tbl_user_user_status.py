# Generated by Django 5.1.3 on 2024-12-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_tbl_user_delete_tbl_guestreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_user',
            name='user_status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
