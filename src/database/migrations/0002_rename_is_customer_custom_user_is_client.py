# Generated by Django 4.0.5 on 2022-06-12 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custom_user',
            old_name='is_customer',
            new_name='is_client',
        ),
    ]
