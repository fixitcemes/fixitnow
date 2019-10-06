# Generated by Django 2.2.3 on 2019-10-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('employed_science', models.DateField()),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_device_name', models.CharField(max_length=100)),
                ('short_name_device', models.CharField(default='Maszyna', max_length=7)),
                ('who_is_made', models.CharField(max_length=100)),
                ('additional_notes', models.TextField(help_text='Type all important information about.', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a occupation (e.g. Manager, Mechanic, Electrican', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('prod_year', models.DateTimeField()),
                ('worked_science', models.DateField()),
                ('short_name_device_own', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dokumenty.DeviceType')),
            ],
        ),
        migrations.CreateModel(
            name='CrashReport',
            fields=[
                ('number_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_notice', models.DateField()),
                ('which_shift', models.CharField(blank=True, choices=[('I', 'Zmiana I (6:00 - 14:00)'), ('II', 'Zmiana II (14:00 - 22:00)'), ('III', 'Zmiana III (22:00 - 06:00)')], default='I', help_text='Zmiana.', max_length=1)),
                ('description', models.TextField(help_text='Please type what happened', max_length=1000)),
                ('status_notice', models.CharField(blank=True, choices=[('o', 'Otwarty'), ('p', 'Przetwarzanie'), ('z', 'Zakonczony')], default='o', help_text='Status dokumentu.', max_length=1)),
                ('which_stuff', models.ManyToManyField(help_text='Select a exactly devices', to='dokumenty.Device')),
                ('who_notice', models.ManyToManyField(help_text='Select a occupation for this employee', to='dokumenty.Author')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='occupation',
            field=models.ManyToManyField(help_text='Select a occupation for this employee', to='dokumenty.Occupation'),
        ),
    ]
