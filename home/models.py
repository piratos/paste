from django.db import models


class Paste(models.Model):
	name = models.CharField(max_length=128)
	code = models.TextField(blank=True)

	def __unicode__(self):
		return "paste number "+str(self.pk)
