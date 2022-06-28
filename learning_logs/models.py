from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
	"""chozen topic"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE) # each user can have his own set of topics

	def __str__(self):
		"""model as text"""
		return self.text

class Entry(models.Model):
	"""info the user learned"""
	topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		"""for django to write plural"""
		verbose_name_plural = 'entries'
		
	def __str__(self):
		"""model as text"""
		if len(self.text) < 50:
			return self.text
		else:
			return f"{self.text[:50]} ..."

