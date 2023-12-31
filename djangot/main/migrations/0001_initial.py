# Generated by Django 4.2.3 on 2023-08-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerid', models.CharField(max_length=100)),
                ('applicant_name', models.CharField(max_length=200)),
                ('applicant_email', models.CharField(max_length=300)),
                ('date', models.TimeField(default=None)),
                ('status', models.CharField(default='unviewd', max_length=100)),
            ],
            options={
                'db_table': 'applications',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('start', models.DateTimeField(max_length=400)),
                ('deadline', models.DateTimeField(max_length=400)),
                ('title', models.CharField(max_length=400)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'offers',
            },
        ),
    ]
