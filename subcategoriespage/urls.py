from django.urls import path
from subcategoriespage.views import (
    SubCategoriesFrequentlyAskedQuestionAPIView,
)


urlpatterns = [
    path('get/subcategories/frequently/asked/questions/',
         SubCategoriesFrequentlyAskedQuestionAPIView.as_view(), name='sub-categories-page'),
]
