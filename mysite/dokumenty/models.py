from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse


class Occupation(models.Model):
    """Model representing a occupation."""
    name = models.CharField(max_length=200, help_text='Enter a occupation (e.g. Manager, Mechanic, Electrican')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class DeviceType(models.Model):
    """Model representing a device type."""
    type_device_name = models.CharField(max_length=100)
    short_name_device = models.CharField(max_length=7, default='Maszyna')
    who_is_made = models.CharField(max_length=100)
    additional_notes = models.TextField(max_length=1000, help_text="Type all important information about.")

    def __str__(self):
        """String for representing the Model object."""
        return self.short_name_device


class Device(models.Model):
    """Model representing a device."""
    type_name = models.ManyToManyField(DeviceType, help_text='Select a device type')
    device_id = models.DecimalField(max_digits=4, decimal_places=0)
    short_name_device_own = ForeignKey(DeviceType, related_name='device_type_device', on_delete=models.SET_NULL,
                                       null=True)
    prod_year = models.DateTimeField(auto_now=False, auto_now_add=False)
    worked_science = models.DateField(auto_now=False)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.short_name_device_own} - {self.device_id}'


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.ManyToManyField(Occupation, help_text='Select a occupation for this employee')
    employed_science = models.DateField(auto_now=False)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class UsedPart(models.Model):
    name_part = models.CharField(max_length=100)
    number_part = models.CharField(max_length=100)
    prize_part = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name_part} {self.number_part} ({self.prize_part} PLN)'

class CrashReport(models.Model):
    number_id = models.AutoField(primary_key=True)
    date_notice = models.DateField(auto_now=False, auto_now_add=False)

    SHIFT_NUMBER = (

        ('I', 'Zmiana I (6:00 - 14:00)'),
        ('II', 'Zmiana II (14:00 - 22:00)'),
        ('III', 'Zmiana III (22:00 - 06:00)'),

    )

    which_shift = models.CharField(
        max_length=3,
        choices=SHIFT_NUMBER,
        blank=True,
        default='I',
        help_text='Zmiana.'
    )

    who_notice = models.ManyToManyField(Author, help_text='Select a occupation for this employee')
    description = models.TextField(max_length=1000, help_text='Please type what happened')
    which_stuff = models.ManyToManyField(Device, help_text='Select a exactly devices')

    PROCESSING_STATUS = (
        ('o', 'Otwarty'),
        ('p', 'Przetwarzanie'),
        ('z', 'Zakonczony'),
    )

    status_notice = models.CharField(
        max_length=1,
        choices=PROCESSING_STATUS,
        blank=True,
        default='o',
        help_text='Status dokumentu.'
    )

    #def display_stuff(self):
    #    return ', '.join([device.name for device in self.device.all()[5:9]])

    def __str__(self):
        return f'ZGL /{self.number_id} / {self.which_stuff.all()} / {self.date_notice}'

    def get_absolute_url(self):
        return reverse('crashreport-detail', args=[str(self.number_id)])


class ServiceReport(models.Model):
    number_id = models.AutoField(primary_key=True)
    date_notice = models.DateField(auto_now=False, auto_now_add=False)

    SHIFT_NUMBER = (
        ('I', 'Zmiana I (6:00 - 14:00)'),
        ('II', 'Zmiana II (14:00 - 22:00)'),
        ('III', 'Zmiana III (22:00 - 06:00)'),

    )

    which_shift = models.CharField(
        max_length=3,
        choices=SHIFT_NUMBER,
        blank=True,
        default='I',
        help_text='Zmiana.'
    )
    who_fixed = models.ManyToManyField(Author, help_text='Select a occupation for this employee')
    who_made = models.ManyToManyField(Author, help_text='Select employee', related_name="author_servicereport_set")
    description = models.TextField(max_length=1000, help_text='Please type what happened')
    which_stuff = models.ManyToManyField(Device, help_text='Select exactly devices')
    used_parts = models.ManyToManyField(UsedPart, help_text="Select used parts")


    PROCESSING_STATUS = (
        ('o', 'Otwarty'),
        ('p', 'Przetwarzanie'),
        ('z', 'Zakonczony'),
    )

    status_notice = models.CharField(
        max_length=1,
        choices=PROCESSING_STATUS,
        blank=True,
        default='o',
        help_text='Status dokumentu.'
    )

    def status_notice_display(self):
        return self.status_notice

    def which_shift_display(self):
        return self.which_shift



    #def display_stuff(self):
    #    return ', '.join([device.name for device in self.device.all()[5:9]])

    def __str__(self):
        return f'RZM/{self.number_id} / {self.which_stuff.all()} / {self.date_notice}'

    def get_absolute_url(self):
        return reverse('servicereport-detail', args=[str(self.number_id)])


