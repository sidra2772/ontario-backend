from rest_framework import serializers
from .models import (
    SubCategoriesQuestionAndAnswer,
    SubCategoriesFrequentlyAskedQuestion,
)


class SubCategoriesQuestionAndAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoriesQuestionAndAnswer
        fields = "__all__"


class SubCategoriesFrequentlyAskedQuestionSerializer(serializers.ModelSerializer):

    sub_categories_frequently_asked_questions = SubCategoriesQuestionAndAnswerSerializer(
        many=True)

    class Meta:
        model = SubCategoriesFrequentlyAskedQuestion
        fields = "__all__"
