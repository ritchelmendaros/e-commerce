from django.db import models


class CustomerTicket(models.Model):
    ticket_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('Account.User', on_delete=models.CASCADE)
    ticket_description = models.CharField(max_length=300)
    ticket_date = models.DateField()
    issue_choices = [
        ("O", "Open"),
        ("C", "Closed"),
    ]
    issue_status = models.CharField(max_length=2, choices=issue_choices)


class TicketCategory(models.Model):
    CATEGORY_CHOICES = [
        ("P", "Payment"),
        ("D", "Delayed"),
        ("S", "Shipment"),
        ("RF", "Refunds"),
        ("RT", "Returns"),
        ("AA", "Account Access"),
        ("AS", "Account Security"),
    ]
    ticket_category_id = models.BigAutoField(primary_key=True)
    ticket_id = models.ForeignKey(CustomerTicket, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = 'Ticket category'


