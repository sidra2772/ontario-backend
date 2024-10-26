from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import SubCategoriesFrequentlyAskedQuestion
from .serializers import SubCategoriesFrequentlyAskedQuestionSerializer


class SubCategoriesFrequentlyAskedQuestionAPIView(APIView):
    """
    How It Works Header For Client API View how it works page
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        how_it_works_header_for_client_object = SubCategoriesFrequentlyAskedQuestion.objects.last()
        serializer = SubCategoriesFrequentlyAskedQuestionSerializer(
            how_it_works_header_for_client_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
