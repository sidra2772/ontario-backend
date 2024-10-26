from django.db import models
from coresite.mixin import AbstractTimeStampModel


class BlogPost(AbstractTimeStampModel):
	title = models.CharField(max_length=50)
	body = models.TextField(max_length=5000, null=False, blank=False)
	image = models.ImageField(upload_to="blog/images/", null=True, blank=False)
	author = models.ForeignKey("userprofile.UserProfile", on_delete=models.CASCADE)
	blog_category = models.ForeignKey("assets.Categories", on_delete=models.CASCADE, related_name='blog_posts')
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title
