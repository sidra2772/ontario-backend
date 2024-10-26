from django.contrib import admin
from .models import Banner, FrequentlyAskedQuestion, QuestionAndAnswer, SocialMedia


class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')


class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ('main_heading', 'sub_heading')
    search_fields = ('main_heading', 'sub_heading')
    list_filter = ('created_at', 'updated_at')


class QuestionAndAnswerAdmin(admin.ModelAdmin):
    list_display = ('frequently_asked_questions', 'question', 'answer')
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name', 'link')
    list_filter = ('created_at', 'updated_at')
