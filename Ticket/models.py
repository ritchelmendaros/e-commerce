from django.db import models


class CustomerTicket(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('Account.CustomerSupport', on_delete=models.CASCADE)
    ticket_description = models.CharField(max_length=300)
    ticket_date = models.DateField()
    issue_choices = [
        ("O", "Open"),
        ("IP", "In Progress"),
        ("C", "Closed"),
    ]
    issue_status = models.CharField(max_length=2, choices=issue_choices)


class TicketCategory(models.Model):
    ticket_category_id = models.BigAutoField(primary_key=True)
    ticket_id = models.ForeignKey(CustomerTicket, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Ticket category'


