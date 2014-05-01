from django.db import models

# Create your models here.
class articles(models.Model):
	level = models.CharField(max_length = 20, primary_key = True)
	articleText = models.TextField()
	imagePath = models.URLField()