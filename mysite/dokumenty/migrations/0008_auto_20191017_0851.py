# Generated by Django 2.2.3 on 2019-10-17 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dokumenty', '0007_servicereport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicereport',
            old_name='who_notice',
            new_name='who_fixed',
        ),
    ]