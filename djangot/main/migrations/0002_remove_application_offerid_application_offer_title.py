# Generated by Django 4.2.3 on 2023-08-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='offerid',
        ),
        migrations.AddField(
            model_name='application',
            name='offer_title',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]