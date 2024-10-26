from rest_framework import viewsets
from rest_framework import permissions
from categoriespage.models import HeaderforCategoriesPage, FooterForCategories
from subcategoriespage.models import (
    SubCategoriesFooter,
    SubCategoriesQuestionAndAnswer,
    SubCategoriesFrequentlyAskedQuestion,
)
from adminDashboard.serializers import HeaderForCategoriesPageSerializer, FooterForCategoriesSerializer
from adminDashboard.serializers import (
    SubCategoriesFooterSerializer,
    SubCategoriesQuestionAndAnswerSerializer,
    SubCategoriesFrequentlyAskedQuestionSerializer,
)


class SubCategoriesFooterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Footer for Sub Categories to be viewed or edited.
    """
    queryset = SubCategoriesFooter.objects.all()
    serializer_class = SubCategoriesFooterSerializer
    permission_classes = [permissions.IsAdminUser]


class SubCategoriesQuestionAndAnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Frequently Asked Questions and Answers for Sub Categories to be viewed or edited.
    """
    queryset = SubCategoriesQuestionAndAnswer.objects.all()
    serializer_class = SubCategoriesQuestionAndAnswerSerializer
    permission_classes = [permissions.IsAdminUser]


class SubCategoriesFrequentlyAskedQuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Frequently Asked Questions for Sub Categories to be viewed or edited.
    """
    queryset = SubCategoriesFrequentlyAskedQuestion.objects.all()
    serializer_class = SubCategoriesFrequentlyAskedQuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class HeaderForCategoriesPageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Header for Categories Page to be viewed or edited.
    """
    queryset = HeaderforCategoriesPage.objects.all()
    serializer_class = HeaderForCategoriesPageSerializer
    permission_classes = [permissions.IsAdminUser]


class FooterForCategoriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Footer for Categories Page to be viewed or edited.
    """
    queryset = FooterForCategories.objects.all()
    serializer_class = FooterForCategoriesSerializer
    permission_classes = [permissions.IsAdminUser]
