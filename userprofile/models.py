from django.db import models
from core.models import User
from coresite.mixin import AbstractTimeStampModel

# Create your models here.

ACCOUNT_TYPE_CHOICES = (
    ("business_member", "Business Member"),
    ("individual", "Individual"),
    ("business_admin", "Business Admin"),
)


class BusinessProfile(AbstractTimeStampModel):
    business_name = models.CharField(max_length=255, unique=True)
    business_domain = models.URLField(max_length=255, unique=True)


class UserProfile(AbstractTimeStampModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    account_type = models.CharField(max_length=255, choices=ACCOUNT_TYPE_CHOICES, default='individual')
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    country_code = models.ForeignKey('assets.CallingCodeWithName', on_delete=models.CASCADE,
                                     related_name='user_country_codes',
                                     null=True, blank=True)
    business_profile = models.ForeignKey('userprofile.BusinessProfile', on_delete=models.CASCADE,
                                         related_name='user_business_profiles', null=True, blank=True)
    country = models.ForeignKey('assets.Countries', on_delete=models.CASCADE, related_name='user_countries',
                                null=True,
                                blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    timezone = models.ForeignKey('assets.CountryTimeZone', on_delete=models.CASCADE, related_name='user_timezones',
                                 null=True, blank=True)
    po_box_number = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.first_name

    def profile_status(self):
        percentage = 0
        if self.first_name and self.last_name:
            percentage += 10
        if self.phone and self.address and self.city and self.country:
            percentage += 20
        if self.image:
            percentage += 20
        if self.timezone:
            percentage += 20
        if self.description:
            percentage += 10
        if self.po_box_number:
            percentage += 10
        if self.title:
            percentage += 10
        return percentage
