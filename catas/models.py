from django.db import models

class Cata(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=True,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	date=models.DateTimeField(blank=True)
	duration = models.CharField(max_length=50)


	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
	