# Generated by Django 4.2.5 on 2023-10-10 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketcategory',
            options={'verbose_name_plural': 'Ticket category'},
        ),
        migrations.RemoveField(
            model_name='customerticket',
            name='ticket_category_id',
        ),
    ]
