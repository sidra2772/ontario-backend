from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Orders(AbstractTimeStampModel):
    """
            This model is used to store the offers sent by freelancer to buyer
        """

    STATUS_CHOICE = (
        ("pending", "Pending"),
        ("canceled", "Canceled"),
        ("rejected", "Rejected"),
        ("completed", "Completed"),

        ('refunded', 'Refunded'),
        ("in_progress", "in_progress"),
        ("in_revision", "In Revision"),
        ("withdraw", "Withdraw"),

    )
    JOB_OFFER_STATUS = (
        ('blocked', 'Blocked'),
        ('unblocked', 'Unblocked'),
    )
    PAYMENT_VIA = (
        ("paypal", "Paypal"),
        ("stripe", "Stripe"),
    )
    PAYMENT_STATUS = (
        ("pending", "Pending"),
        ('paid', 'Paid'),
        ('overdue', 'overdue'),
    )
    client = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='client_offer', null=True, blank=True)
    job = models.ForeignKey(
        "jobs.Jobs", on_delete=models.CASCADE, related_name='job_offer', null=True, blank=True)
    service = models.ForeignKey(
        "services.Services", on_delete=models.CASCADE, related_name='service_offer')
    is_custom_offer = models.BooleanField(default=False)
    payment_via = models.CharField(
        max_length=255, choices=PAYMENT_VIA, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICE, default="in_progress")
    cancel_reason = models.TextField(null=True, blank=True)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_number = models.CharField(max_length=50, unique=True, primary_key=True)
    payment_status = models.CharField(
        max_length=255, choices=PAYMENT_STATUS, default="pending")
    is_paid_service_fee = models.BooleanField(default=False)
    hiring_date = models.DateTimeField(null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    service_fee = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Orders'
        db_table = 'orders'
