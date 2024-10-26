from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Applications(AbstractTimeStampModel):
    service = models.ForeignKey('services', on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='applications')
    title = models.CharField(max_length=255)
    cost_estimate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    attachments = models.FileField(upload_to='applications/attachments/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Applications'
        db_table = 'applications'

    def __str__(self):
        return self.title