from django.db import models


class TicketCategory(models.Model):
    ticket_category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Ticket category'


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
    ticket_category_id = models.ForeignKey(TicketCategory, models.SET_NULL, null=True)


class TicketReply(models.Model):
    reply_id = models.BigAutoField(primary_key=True)
    replycontent = models.CharField(max_length=500)
    user_id = models.ForeignKey('Account.User', on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(CustomerTicket, models.SET_NULL, null=True)
    support_name = models.CharField(max_length=50)