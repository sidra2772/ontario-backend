from django.urls import path
from homePage.views import BannerAPIView, FrequentlyAskedQuestionAPIView, SocialMediaAPIView

urlpatterns = [
    path('get/banner/', BannerAPIView.as_view(), name='banner'),
    path('get/frequently/asked/questions/', FrequentlyAskedQuestionAPIView.as_view(),
         name='frequently-asked-questions'),
    path('get/social/media/', SocialMediaAPIView.as_view(), name='social-media'),

]
