# Generated by Django 3.1 on 2022-08-29 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20220829_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='_id',
            new_name='geo_tab_id',
        ),
    ]
