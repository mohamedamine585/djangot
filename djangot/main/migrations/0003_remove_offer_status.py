# Generated by Django 4.2.3 on 2023-08-02 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_application_offerid_application_offer_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='status',
        ),
    ]
