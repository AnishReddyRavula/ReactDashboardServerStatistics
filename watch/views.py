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
	return JsonResponse([{'student':'Cool stuff'}, {'fo':'fafa'}, {'student':'Cool stuff'}, {'fo':'fafa'}], safe=False)



