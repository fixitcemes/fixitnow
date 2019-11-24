# Generated by Django 2.2.3 on 2019-10-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokumenty', '0011_auto_20191017_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicereport',
            name='who_made',
            field=models.ManyToManyField(help_text='Select employee', related_name='author_servicereport_set', to='dokumenty.Author'),
        ),
    ]