# Generated by Django 4.2.5 on 2023-10-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_customersupport_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.CharField(default='CS', max_length=2),
        ),
    ]
