# Generated by Django 4.2.5 on 2023-11-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0005_alter_customerticket_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcategory',
            name='category_name',
            field=models.CharField(choices=[('P', 'Payment'), ('D', 'Delayed'), ('S', 'Shipment'), ('RF', 'Refunds'), ('RT', 'Returns'), ('AA', 'Account Access'), ('AS', 'Account Security')], max_length=2),
        ),
    ]
