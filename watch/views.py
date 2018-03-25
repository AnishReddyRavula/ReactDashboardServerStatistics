from django.shortcuts import render
from django.http import HttpResponse
# from watch.models import server_desc
from django.http import JsonResponse
import json
from rest_framework import generics #This module helps us to handle get, post, dlete, put requests
from watch.models import ServerDetails
from watch.models import ServerUsage 
from djreact.serializers import DetailSerializer
from djreact.serializers import UsageSerializer #Serializer to map the Model instance into JSON format
import pandas as pd
from watch.models import ServerDetails
from time import time
from collections import OrderedDict
# from watch.models import ServerUsage
# 
def parse_csv(request, company=None):
	"""
	Parse the respective company's server csv file (all attributes)
	"""
	import glob, os # glob to search and os to get the directory files
	import csv 
	from datetime import datetime
	
	files = []
	dates = []
	

	def time_change(data):
		"""
		To convert string to datetime object
		"""
		return datetime.strptime(data, '%a %b %d  %X %Y')


	# if there is no company attribute in url return false
	if company is  None:
		return render(request, 'watch/result.html', {"result":False}) 

	else:
		for file in glob.glob("data/"+company+"*"): # Go to every file in the directory and save the path in a list
			f = open(file, 'r')
			files.append(file)
			f.close()

		for file in files:
			# used pandas here to parse the csv as it is faster and more convinient
			f = pd.read_csv(file)
			f = f.set_index('Server id') # set serverid as index
			f.columns = f.columns.map(time_change) # change all the time strings to datetime objects
			servers = f.index.values # get all the servers
			print(company)
			#To get the company and department name in correct title format
			spl = file[:-4].split("-")[-2:]
			department = "_".join(spl).upper()
			print(department)
			if ServerDetails.objects.filter(department_name = company, metric = department).count() == 0:	

				# Make server details object				
				server_entry = ServerDetails()
				server_entry.department_name = company
				server_entry.metric = department
				server_entry.save()
				f = f.transpose()
				instances = []
				batch_size = 100

				# get the server detail object to reference in server usage
				server_details = ServerDetails.objects.get(department_name = company, metric = department)
				for server in servers: #go to every server and get the details and do not save the usage if the data is NULL
					print(server)
					for index, row in f[server].iteritems():
							if not pd.isnull(row):
								instances.append(ServerUsage(server_name = server, detail = server_details, date_time = index, units = row))

				# save all the insert queries in array and excute later at a single transaction using bulk create
				# saves time and memory usage
				ServerUsage.objects.bulk_create(instances, batch_size)
		return render(request, 'watch/result.html', {"result":files}) 












def index(request):
	"""
	index page to render all the details of the companies
	"""

	start = time() # time to track the rendering time
	companies = ServerDetails.objects.order_by().values('department_name').distinct()
	companies = [ x['department_name'] for x in companies]
	company = OrderedDict()
	for i in companies:
		company[i] = i.title()

	#server list hardcoded for fast can make another table to make it fast
	servers_list = {"finance": ["Mean","finance-server-medium-0", "finance-server-light-1", "finance-server-medium-2"], "python": ["Mean","python-apps-server-medium-0", "python-apps-server-light-1", "python-apps-server-heavy-2", "python-apps-server-light-3", "python-apps-server-light-4"], "front-end": ["Mean", "front-end-server-light-0", "front-end-server-heavy-1", "front-end-server-light-2", "front-end-server-medium-3", "front-end-server-medium-4", "front-end-server-medium-5", "front-end-server-medium-6", "front-end-server-light-7", "front-end-server-heavy-8", "front-end-server-light-9", "front-end-server-light-10", "front-end-server-medium-11", "front-end-server-light-12", "front-end-server-light-13", "front-end-server-light-14"], "ops": ["Mean", "ops-server-light-0", "ops-server-medium-1", "ops-server-light-2", "ops-server-medium-3", "ops-server-medium-4"], "java": ["Mean","java-apps-server-medium-0", "java-apps-server-light-1", "java-apps-server-light-2", "java-apps-server-medium-3", "java-apps-server-heavy-4", "java-apps-server-medium-5", "java-apps-server-light-6", "java-apps-server-light-7", "java-apps-server-medium-8", "java-apps-server-medium-9"]}

	total_time = time() - start
	print(total_time) # total time taken to complete the request
	return render(request, "watch/home.html", context = {'args':'lok', 'companies':company, 'servers':json.dumps(servers_list)})

def get_data(request, company=None, metric=None, server=None):


	from django.db.models import Count, Avg
	from time import mktime
	start = time()
	returning_json = OrderedDict()

	if metric is not None:
		metrics = [metric]
	else:
		metrics = ["AVG_CPU","AVG_RAM","DISK_USED","MAX_CPU","MAX_RAM"]

	for metric in metrics:
		returning_json[metric] = OrderedDict()
	if company is not None:
		for metric_temp in metrics:
			if (server) and (server != 'Mean'):
				print(company, metric_temp, server)
				server_usage = ServerUsage.objects.filter(detail_id__department_name = company, detail_id__metric = metric_temp, server_name = server).order_by('date_time').annotate(dcount = Count('date_time')).values('date_time').annotate(score = Avg('units'))	
			elif server is 'Mean':
				print(company, metric_temp)
				server_usage = ServerUsage.objects.filter(detail_id__department_name = company, detail_id__metric = metric_temp).order_by('date_time').annotate(dcount = Count('date_time')).values('date_time').annotate(score = Avg('units'))	
			else:
				server_usage = ServerUsage.objects.filter(detail_id__department_name = company, detail_id__metric = metric_temp).order_by('date_time').annotate(dcount = Count('date_time')).values('date_time').annotate(score = Avg('units'))
			date_ = []
			usage = []
			print(server_usage)
			for each_server in server_usage:
				date_.append(each_server['date_time'])
				usage.append(each_server['score'])
			returning_json[metric_temp]['date_time'] = date_
			returning_json[metric_temp]['usage'] = usage
	total_time = time() - start
	print(total_time)
	return JsonResponse(returning_json, safe=False)



