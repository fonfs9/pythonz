# Generated by Django 3.0.3 on 2020-02-24 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0047_auto_20200224_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancy',
            old_name='url_site',
            new_name='url',
        ),

    ]
