# Generated by Django 2.2.5 on 2019-09-18 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20190918_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='track',
            new_name='tracks',
        ),
    ]
