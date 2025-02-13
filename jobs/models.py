from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Jobs(AbstractTimeStampModel):
    title = models.CharField(max_length=255)
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)
    description = models.TextField()
    bit_type = models.CharField(max_length=255, null=True, blank=True)
    job_price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255, null=True, blank=True)
    bid_closing_date = models.DateTimeField()
    duration_in_months = models.PositiveIntegerField()
    submission_type = models.CharField(max_length=255)
    condition_for_participation = models.TextField()
    agreement = models.FileField(upload_to='jobs/agreements/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Jobs'
        db_table = 'jobs'


class JobBids(AbstractTimeStampModel):
    job = models.ForeignKey('jobs.Jobs', on_delete=models.CASCADE, related_name='bids')
    bidder = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='bids', null=True, blank=True)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='jobs/bids/', blank=True, null=True)
    bid_description = models.TextField()
    due_date = models.DateTimeField()
    cover_letter = models.TextField()

    class Meta:
        verbose_name_plural = 'Job Bids'
        db_table = 'job_bids'