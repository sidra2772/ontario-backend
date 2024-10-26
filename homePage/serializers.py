from rest_framework import serializers
from .models import (
    Banner,
    FrequentlyAskedQuestion,
    QuestionAndAnswer,
    SocialMedia,
)


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class QuestionAndAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAndAnswer
        fields = "__all__"


class FrequentlyAskedQuestionSerializer(serializers.ModelSerializer):
    question_and_answer = QuestionAndAnswerSerializer(many=True)

    class Meta:
        model = FrequentlyAskedQuestion
        fields = "__all__"


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"
