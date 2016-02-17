from django.shortcuts import render
from django.template.loader import get_template
import urllib2
import json
from django.http import HttpResponse

locu_api = "74778249bf8fe8092300d0b0aa2933846efa98c8"

json_obj = urllib2.urlopen('https://api.locu.com/v1_0/venue/search/?locality=seattle&api_key=74778249bf8fe8092300d0b0aa2933846efa98c8')

data=json.load(json_obj)

for item in data['objects']:
	name = item['name']
	phone = item['phone']

def home(request):
	return HttpResponse(name phone)
