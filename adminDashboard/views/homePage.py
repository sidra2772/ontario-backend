from homePage.models import Banner, FrequentlyAskedQuestion, QuestionAndAnswer, SocialMedia
from homePage.serializers import BannerSerializer, FrequentlyAskedQuestionSerializer, QuestionAndAnswerSerializer, \
    SocialMediaSerializer
from rest_framework import viewsets


class BannerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Banners.
    """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class FrequentlyAskedQuestionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Frequently Asked Questions.
    """
    queryset = FrequentlyAskedQuestion.objects.all()
    serializer_class = FrequentlyAskedQuestionSerializer


class SocialMediaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Social Media.
    """
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
