from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Banner(AbstractTimeStampModel):
    """
    Banner Model
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='banner/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'


class FrequentlyAskedQuestion(AbstractTimeStampModel):
    """
    Frequently Asked Questions Model
    """
    main_heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)

    def __str__(self):
        return self.main_heading

    class Meta:
        ordering = ('created_at',)


class QuestionAndAnswer(AbstractTimeStampModel):
    """
    Frequently Asked Questions and Answers Model
    """
    frequently_asked_questions = models.ForeignKey(
        'homePage.FrequentlyAskedQuestion', on_delete=models.CASCADE, related_name='frequently_asked_questions')
    question = models.CharField(max_length=1000)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        ordering = ('created_at',)


class SocialMedia(AbstractTimeStampModel):
    """
    Social Media Model
    """
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
