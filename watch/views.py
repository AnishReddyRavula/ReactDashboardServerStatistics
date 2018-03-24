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
# Parse the respective company's server csv file (all attributes)
def parse_csv(request, company=None):
	import glob, os # glob to search and os to get the directory files
	import csv
	files = []
	dates = []
	a = 'h'
	from collections import defaultdict, Counter
	from datetime import datetime
	# def make_none(data):
	# 	if 
	# 	return None
	def time_change(data):
		return datetime.strptime(data, '%a %b %d  %X %Y')
	domain_counts = defaultdict(Counter)
	# if there is no company attribute in url
	if company is  None:
		return render(request, 'watch/result.html', {"result":False}) 
	else:
		for file in glob.glob("data/"+company+"*"):
			f = open(file, 'r')
			files.append(file)
			f.close()
		datetime_object = []
		for file in files:
			f = pd.read_csv(file)
			f = f.set_index('Server id')
			f.columns = f.columns.map(time_change)
			servers = f.index.values
			print(company)
			spl = file[:-4].split("-")[-2:]
			department = "_".join(spl).upper()
			print(department)
			if ServerDetails.objects.filter(department_name = company, metric = department).count() == 0:					
				server_entry = ServerDetails()
				server_entry.department_name = company
				server_entry.metric = department
				server_entry.save()
			f = f.transpose()
			instances = []
			batch_size = 100
			server_details = ServerDetails.objects.get(department_name = company, metric = department)
			for server in servers:
				print(server)
				for index, row in f[server].iteritems():
						if not pd.isnull(row):
							instances.append(ServerUsage(server_name = server, detail = server_details, date_time = index, units = row))
			ServerUsage.objects.bulk_create(instances, batch_size)
				
				# for entry in dt:
				# 	check = pd.isnull(entry)
				# 	if check:
				# 		print(entry, "---------")
				# 		continue
				# 	else:
				# 		print(entry.column)
				# 		break
				# break
						# server_details = ServerDetails.objects.get(department_name = company, metric = department)
						# server_usage = ServerUsage()
						# server_usage.detail = server_details
						# server_usage.date_time = entry
						# server_usage.units = 
						


		return render(request, 'watch/result.html', {"result":files}) 








def submit_request(request):
	print(request.GET)
	print(request.GET['ap'])
	if request.GET['ap'] == 'BT':
		return JsonResponse([{'student':'Cool stuff'}, {'fo':'fafa'}, {'student':'Cool stuff'}, {'fo':'fafa'}], safe=False)
	if request.GET['ap'] == 'sales':
		return JsonResponse({"cool":[{
			'label': 'mast Central',
			'value': '580000'
		}, {
			'label': 'mast Groove harbour',
			'value': '630000'
		}, {
			'label': 'Los mast Topanga',
			'value': '790000'
		}, {
			'label': 'mast-Rancho Dom',
			'value': '420000'
		}, {
			'label': 'Daly Cisdfty mast',
			'value': '630000'
		}], "title":"New Caption"}, safe=False)

	else:
		return JsonResponse({"cool":[{
			'label': 'anish Central',
			'value': '880000'
		}, {
			'label': 'anish Groove harbour',
			'value': '730000'
		}, {
			'label': 'Los anish Topanga',
			'value': '790000'
		}, {
			'label': 'anish-Rancho Dom',
			'value': '520000'
		}, {
			'label': 'Daly Cisdfty anish',
			'value': '330000'
		}], "title":"Old Caption"}, safe=False)


def options(request):

	return JsonResponse([{'student':'Cool stuff'}, {'fo':'fafa'}, {'studenta':'Cool stuff'}, {'fo':'fafa'}], safe=False)



class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	""" This class handles the http GET, PUT and DELETE requests."""

	queryset = ServerUsage.objects.all()
	serializer_class = UsageSerializer

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def snippet_list(request):
	if request.method == 'GET':
		snippets = ServerUsage.objects.all()
		serializer = UsageSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)

def index(request):
	start = time()
	companies = ServerDetails.objects.order_by().values('department_name').distinct()
	# servers = ServerUsage.objects.filter(detail_id__department_name = companies[0]['department_name']).values('server_name').distinct()
	# print(servers)
	companies = [ x['department_name'] for x in companies]
	company = OrderedDict()
	for i in companies:
		company[i] = i.title()

	# companies = ServerDetails.objects.all().values('department_name').distinct()
	# di = OrderedDict()
	# for comp in companies:
	# 	servers = ServerUsage.objects.filter(detail_id__department_name = comp['department_name']).values('server_name').distinct()
	# 	servers = [x['server_name'] for x in servers]
	# 	di[comp['department_name']] = servers
	di = {"finance": ["Mean","finance-server-medium-0", "finance-server-light-1", "finance-server-medium-2"], "python": ["Mean","python-apps-server-medium-0", "python-apps-server-light-1", "python-apps-server-heavy-2", "python-apps-server-light-3", "python-apps-server-light-4"], "front-end": ["Mean", "front-end-server-light-0", "front-end-server-heavy-1", "front-end-server-light-2", "front-end-server-medium-3", "front-end-server-medium-4", "front-end-server-medium-5", "front-end-server-medium-6", "front-end-server-light-7", "front-end-server-heavy-8", "front-end-server-light-9", "front-end-server-light-10", "front-end-server-medium-11", "front-end-server-light-12", "front-end-server-light-13", "front-end-server-light-14"], "ops": ["Mean", "ops-server-light-0", "ops-server-medium-1", "ops-server-light-2", "ops-server-medium-3", "ops-server-medium-4"], "java": ["Mean","java-apps-server-medium-0", "java-apps-server-light-1", "java-apps-server-light-2", "java-apps-server-medium-3", "java-apps-server-heavy-4", "java-apps-server-medium-5", "java-apps-server-light-6", "java-apps-server-light-7", "java-apps-server-medium-8", "java-apps-server-medium-9"]}
	total_time = time() - start
	print(total_time)
	return render(request, "watch/home.html", context = {'args':'lok', 'companies':company, 'servers':json.dumps(di)})

def get_data(request, company=None, metric=None, server=None ):


	from django.db.models import Count, Avg
	from time import mktime
	start = time()
	print(start)
	print(company)
	print(server)
	# start = request.GET.get('start', None)
	# end = request.GET.get('end', None)
	returning_json = OrderedDict()

	if metric is not None:
		metrics = [metric]
	else:
		metrics = ["AVG_CPU","AVG_RAM","DISK_USED","MAX_CPU","MAX_RAM"]

	for metric in metrics:
		returning_json[metric] = OrderedDict()

	if company is not None:

		for metric in metrics:
			if server is not None:
				server_usage = ServerUsage.objects.filter(detail_id__department_name = company, detail_id__metric = metric, server_name = server).order_by('date_time').annotate(dcount = Count('date_time')).values('date_time').annotate(score = Avg('units'))	
			else:
				server_usage = ServerUsage.objects.filter(detail_id__department_name = company, detail_id__metric = metric).order_by('date_time').annotate(dcount = Count('date_time')).values('date_time').annotate(score = Avg('units'))
			date_ = []
			usage = []
			for each_server in server_usage:
				date_.append(each_server['date_time'])
				usage.append(each_server['score'])
			returning_json[metric]['date_time'] = date_
			returning_json[metric]['usage'] = usage
				# returning_json[metric].append([mktime(server['date_time'].timetuple()), server['score']])
	# ServerUsage.objects.filter(detail_id__department_name = company.lower()).values('date_time', 'units')
	total_time = time() - start
	print(total_time)
	return JsonResponse(returning_json, safe=False)


def get_servers(request):

	companies = ServerDetails.objects.all().values('department_name').distinct()
	di = OrderedDict()
	for company in companies:
		d = ['']
		servers = ServerUsage.objects.filter(detail_id__department_name = company['department_name']).values('server_name').distinct()
		d = d.append(servers)
		servers = [x['server_name'] for x in servers]
		di[company['department_name']] = d
	# server = OrderedDict()
	# for i,x in enumerate(servers):
	# 	server[x] = " ".join(x.split('-')).title()
	print(di)

	return JsonResponse(di, safe=False)
