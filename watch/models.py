from django.db import models


class ServerDetails(models.Model):
	department_name = models.CharField(max_length=140) #finance
	SERVER_METRICS = (
		('AVG_CPU', 'Avg CPU'),
		('AVG_RAM', 'Avg RAM'),
		('DISK_USED', 'Disk Usage'),
		('MAX_CPU', 'Max CPU'),
		('MAX_RAM', 'Max RAM'),
	)
	metric = models.CharField(max_length=140, choices=SERVER_METRICS) #avg-cpu

	def __str__(self):
		return str(self.department_name)

class ServerUsage(models.Model):
	server_name = models.CharField(max_length=100)
	detail = models.ForeignKey(ServerDetails, on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now=False)
	units = models.PositiveSmallIntegerField()

	def __str__(self):
		return str(self.units)
