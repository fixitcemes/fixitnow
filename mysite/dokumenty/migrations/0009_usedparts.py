# Generated by Django 2.2.3 on 2019-10-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dokumenty', '0008_auto_20191017_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedParts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_part', models.CharField(max_length=100)),
                ('number_part', models.CharField(max_length=100)),
                ('prize_part', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]