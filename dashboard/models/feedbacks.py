from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from coresite.mixin import AbstractTimeStampModel


class ClientFeedback(AbstractTimeStampModel):
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    order = models.OneToOneField(
        'dashboard.Orders', on_delete=models.CASCADE, related_name='order_feedback', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Client Feedback'
        verbose_name_plural = 'Client Feedbacks'


class SupplierFeedback(AbstractTimeStampModel):
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField()
    order = models.OneToOneField(
        'dashboard.Orders', on_delete=models.CASCADE, related_name='order_feedback_supplier', null=True, blank=True)
    service = models.ForeignKey(
        'services.Services', on_delete=models.CASCADE, related_name='service_feedback', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Supplier Feedback'
        verbose_name_plural = 'Supplier Feedbacks'
