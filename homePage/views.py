from rest_framework.views import APIView
from .models import Banner, FrequentlyAskedQuestion, SocialMedia
from rest_framework.generics import ListAPIView
from .serializers import BannerSerializer, FrequentlyAskedQuestionSerializer, SocialMediaSerializer
from rest_framework.response import Response
from rest_framework import status


class BannerAPIView(APIView):
    """ This class is used to fetch all the banners from the database. """
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get(self, request):
        """ This method is used to get the banners from the database. """
        banners = self.queryset
        if banners.exists():
            serializer = BannerSerializer(banners.latest('id'))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No banners found'}, status=status.HTTP_404_NOT_FOUND)


class FrequentlyAskedQuestionAPIView(APIView):
    """ This class is used to fetch all the frequently asked questions from the database. """
    queryset = FrequentlyAskedQuestion.objects.all()
    serializer_class = FrequentlyAskedQuestionSerializer

    def get(self, request):
        """ This method is used to get the frequently asked questions from the database. """
        frequently_asked_questions = self.queryset
        if frequently_asked_questions.exists():
            serializer = FrequentlyAskedQuestionSerializer(frequently_asked_questions.latest('id'), )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'No frequently asked questions found'}, status=status.HTTP_404_NOT_FOUND)


class SocialMediaAPIView(ListAPIView):
    """ This class is used to fetch all the social media links from the database. """
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
