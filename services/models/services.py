from django.db import models
from coresite.mixin import AbstractTimeStampModel
from django.contrib.postgres.fields import ArrayField

SERVICE_STATUS = (
    ('Pending', 'Pending'),
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
    ('Rejected', 'Rejected')
)

AVAILABLE_DAYS = (
    ('all_days', 'All Days'),
    ('week_days', 'Week Days'),
    ('weekend', 'Weekend'),
)


class Services(AbstractTimeStampModel):
    """ This model is used to store the services."""
    sub_category = models.ForeignKey(
        'assets.SubCategories', related_name='servicesSubcategories', on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        'userprofile.UserProfile', related_name='servicesSupplier', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    service_slug = models.SlugField(max_length=255, unique=True)
    service_status = models.CharField(max_length=255, default='Pending', choices=SERVICE_STATUS)
    short_description = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.FileField(upload_to='services', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey('assets.Currency', related_name='servicesCurrency', on_delete=models.CASCADE,
                                 null=True, blank=True)
    attachment = models.FileField(upload_to='services/attachments/', null=True, blank=True)
    tags = ArrayField(
            models.CharField(max_length=10),
            blank=True,
            default=list,
        )
    availability_start_time = models.TimeField(null=True, blank=True)
    availability_end_time = models.TimeField(null=True, blank=True)
    availability_days = models.CharField(max_length=255, choices=AVAILABLE_DAYS, default='all_days')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Services'
        db_table = 'services'
