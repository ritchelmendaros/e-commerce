# Generated by Django 4.2.5 on 2023-11-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0002_alter_ticketcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerticket',
            name='ticket_description',
            field=models.CharField(max_length=300),
        ),
    ]