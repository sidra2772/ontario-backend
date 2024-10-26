from django.urls import path
from categoriespage.views import (
    HeaderforCategoriesPageAPIView,)

urlpatterns = [
    path('get/header/for/categories/page/',
         HeaderforCategoriesPageAPIView.as_view(), name='categories_page'),
]
