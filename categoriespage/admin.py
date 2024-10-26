from django.contrib import admin
from categoriespage.models import (
    HeaderforCategoriesPage,
    FooterForCategories,
)

# Register your models here.

@admin.register(HeaderforCategoriesPage)
class HeaderforCategoriesPageAdmin(admin.ModelAdmin):
    """
    Header for Categories Page Admin
    """

    list_display = (
        'main_heading',
    )

@admin.register(FooterForCategories)
class FooterForCategoriesAdmin(admin.ModelAdmin):
    """
    Footer For Categories Admin
    """

    list_display = (
        'main_heading',
    )