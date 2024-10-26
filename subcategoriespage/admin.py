from django.contrib import admin
from .models import (
    SubCategoriesFooter,
    SubCategoriesQuestionAndAnswer,
    SubCategoriesFrequentlyAskedQuestion,
)

# Register your models here.


@admin.register(SubCategoriesQuestionAndAnswer)
class SubCategoriesQuestionAndAnswerAdmin(admin.ModelAdmin):
    """
    Sub Categories Question And Answer Admin
    """

    list_display = (
        'question',
        'answer',
    )


@admin.register(SubCategoriesFrequentlyAskedQuestion)
class SubCategoriesFrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    """
    Sub Categories Frequently Asked Question Admin
    """

    list_display = (
        'main_heading',
        'sub_heading',
    )


@admin.register(SubCategoriesFooter)
class SubCategoriesFooterAdmin(admin.ModelAdmin):
    """
    Sub Categories Footer Admin
    """

    list_display = (
        'main_heading',
    )
