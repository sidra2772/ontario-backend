import uuid
from django.db import models
from coresite.mixin import AbstractTimeStampModel

SUBJECT_CHOICES = (
    ('other', 'Other'),
    ('bug', 'Bug'),
    ('feature', 'Feature'),
    ('question', 'Question'),
    ('suggestion', 'Suggestion'),
    ('complaint', 'Complaint'),
    ('order_report', 'Order Report'),
)
STATUS_CHOICES = (
    ('closed', 'Closed'),
    ('pending', 'Pending'),
    ('resolved', 'Resolved'),
    ('in_progress', 'In Progress'),

)


class ReportImage(AbstractTimeStampModel):
    file = models.FileField(upload_to='reports/')
    report = models.ForeignKey(
        'helpandsupport.Report', on_delete=models.CASCADE, related_name='report_images')


class Report(AbstractTimeStampModel):
    report_number = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True,
        db_index=True, verbose_name='Report Number', primary_key=True
    )
    reporter = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE,
                                 related_name='user_reports', null=True, blank=True)
    receiver = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE,
                                 related_name='receiver_reports', null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(
        max_length=50, default='other', choices=SUBJECT_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(
        'dashboard.Orders', on_delete=models.CASCADE, related_name='order_reports', null=True, blank=True)
    status = models.CharField(
        max_length=50, default='pending', choices=STATUS_CHOICES)

    def __str__(self):
        return self.subject
