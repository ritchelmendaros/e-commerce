# Generated by Django 4.2.5 on 2023-11-04 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ticket', '0004_alter_customerticket_issue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerticket',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
