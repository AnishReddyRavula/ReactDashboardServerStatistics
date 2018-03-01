from django.db import models


class ServerDetails(models.Model):
	id_no = models.IntegerField()
	department_name = models.CharField(max_length=140) #finance
	metric = models.CharField(max_length=140) #avg-cpu

	def __str__(self):
		return self.department_name, self.metric

class ServerUsage(models.Model):
	entry_id = models.IntegerField()
	detail = models.ForeignKey(ServerDetails, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=False)
	units = models.PositiveSmallIntegerField()
	def __str__(self):
		return self.detail, self.date_time, self.units
