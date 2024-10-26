from django.db import models


class SubCategoriesFrequentlyAskedQuestion(models.Model):
    """
    Frequently Asked Questions for Sub Categories
    """
    main_heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_heading

    class Meta:
        ordering = ('created_at',)


class SubCategoriesQuestionAndAnswer(models.Model):
    """
    Frequently Asked Questions and Answers for Sub Categories
    """
    sub_categories_frequently_asked_questions = models.ForeignKey(
        'subcategoriespage.SubCategoriesFrequentlyAskedQuestion', on_delete=models.CASCADE, related_name='sub_categories_frequently_asked_questions')
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('created_at',)
from django.db import models


class SubCategoriesFooter(models.Model):
    """
    Footer for Sub Categories
    """
    main_heading = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_heading

    class Meta:
        ordering = ('created_at',)
