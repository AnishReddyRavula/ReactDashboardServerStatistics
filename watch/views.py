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
def submit_request(request):
	print(request.GET)
	print(request.GET['ap'])
	if request.GET['ap'] == 'BT':
		return JsonResponse([{'student':'Cool stuff'}, {'fo':'fafa'}, {'student':'Cool stuff'}, {'fo':'fafa'}], safe=False)
	if request.GET['ap'] == 'sales':
		return JsonResponse([{
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
        }], safe=False)

	else:
		return JsonResponse([{
            'label': 'anish Central',
            'value': '880000'
        }, {
            'label': 'anish Groove harbour',
            'value': '730000'
        }, {
            'label': 'Los anish Topanga',
            'value': '590000'
        }, {
            'label': 'anish-Rancho Dom',
            'value': '520000'
        }, {
            'label': 'Daly Cisdfty anish',
            'value': '330000'
        }], safe=False)



