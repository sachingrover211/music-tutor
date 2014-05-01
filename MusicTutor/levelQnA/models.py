from django.db import models

# Create your models here.
class questions(models.Model):
	level = models.ForeignKey('article.articles')
	questions = models.CharField(max_length = 1000)
	qType = models.CharField(max_length=5)
	answer = models.CharField(max_length=1000)
	hints = models.CharField(max_length=500)
	image = models.CharField(max_length=40)