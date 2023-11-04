# Generated by Django 4.2.5 on 2023-11-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0009_alter_ticketcategory_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='category_name',
            field=models.CharField(choices=[('P', 'Payment'), ('D', 'Delayed'), ('S', 'Shipment')], max_length=2),
        ),
    ]