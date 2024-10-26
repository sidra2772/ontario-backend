from rest_framework import serializers
from categoriespage.models import HeaderforCategoriesPage, FooterForCategories
from subcategoriespage.models import (
    SubCategoriesFooter,
    SubCategoriesFrequentlyAskedQuestion,
    SubCategoriesQuestionAndAnswer,
)


class SubCategoriesFrequentlyAskedQuestionSerializer(serializers.ModelSerializer):
    """
    Frequently Asked Questions for Sub Categories
    """

    class Meta:
        model = SubCategoriesFrequentlyAskedQuestion
        fields = '__all__'


class SubCategoriesQuestionAndAnswerSerializer(serializers.ModelSerializer):
    """
    Frequently Asked Questions and Answers for Sub Categories
    """

    class Meta:
        model = SubCategoriesQuestionAndAnswer
        fields = '__all__'


class SubCategoriesFooterSerializer(serializers.ModelSerializer):
    """
    Footer for Sub Categories
    """

    class Meta:
        model = SubCategoriesFooter
        fields = '__all__'


class HeaderForCategoriesPageSerializer(serializers.ModelSerializer):
    """
    Header For Categories Page Serializer
    """

    class Meta:
        model = HeaderforCategoriesPage
        fields = '__all__'


class FooterForCategoriesSerializer(serializers.ModelSerializer):
    """
    Footer For Categories Serializer
    """

    class Meta:
        model = FooterForCategories
        fields = '__all__'
