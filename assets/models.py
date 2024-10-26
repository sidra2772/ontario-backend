from django.db import models
from coresite.mixin import AbstractTimeStampModel


CATEGORY_CHOICES = (
    ("blog" ,"blog"),
    ("service", "service")
)


class Categories(AbstractTimeStampModel):
    index = models.PositiveBigIntegerField(default=0)
    name = models.CharField(max_length=100, unique=True, error_messages={
                            'unique': "This Category has already been registered."})
    category_slug = models.SlugField(max_length=100, unique=True)
    image = models.FileField(upload_to='category', null=True, blank=True)
    category_type = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default=CATEGORY_CHOICES[0][1])
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class SubCategories(AbstractTimeStampModel):
    category = models.ForeignKey(
        'Categories', related_name='sub_categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    subcategory_slug = models.SlugField(max_length=100, unique=True)
    image = models.FileField(upload_to='subcategory', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Sub Categories'
        db_table = 'sub_categories'
        unique_together = ('category', 'name')


class Countries(AbstractTimeStampModel):
    common_name = models.CharField(max_length=255)
    official_name = models.CharField(max_length=255, null=True, blank=True)
    alpha_code_2 = models.CharField(max_length=10, blank=True, null=True)
    alpha_code_3 = models.CharField(max_length=10, blank=True, null=True)
    flag_png = models.CharField(max_length=255, blank=True, null=True)
    flag_svg = models.CharField(max_length=255, blank=True, null=True)
    flag_png_file = models.FileField(max_length=255, blank=True, null=True)
    flag_svg_file = models.FileField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.common_name

    class Meta:
        verbose_name_plural = 'Countries'
        db_table = 'countries'


class CountryTimeZone(AbstractTimeStampModel):
    country = models.ForeignKey(
        'Countries', related_name='timezones', on_delete=models.CASCADE, null=True, blank=True)
    timezone = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.country} - {self.timezone}'


class Currency(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'
        db_table = 'currencies'
        unique_together = ('name', 'code',)


class CallingCodeWithName(AbstractTimeStampModel):
    name = models.CharField(max_length=100)
    calling_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calling_code}  {self.name}"
