from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default = 0)
	
	
	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.name

class Article(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	content = models.TextField()
	views = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')
	
	
	
	def __unicode__(self):		#For Python 2, use __str__ on Python 3
		return self.title