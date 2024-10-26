from django.db import models

# Create your models here.


class HeaderforCategoriesPage(models.Model):
    """
    Header for Categories Page Model
    """
    main_heading = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='categories_page_header/')

    def __str__(self):
        return self.main_heading

    class Meta:
        verbose_name = 'Header for Categories Page'
        verbose_name_plural = 'Header for Categories Page'


class FooterForCategories(models.Model):
    """
    Footer For Categories Model
    """
    main_heading = models.CharField(max_length=100)

    def __str__(self):
        return self.main_heading

    class Meta:
        verbose_name = 'Footer For Categories'
        verbose_name_plural = 'Footer For Categories'
