# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import operator
import urllib
from datetime import datetime

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.http import HttpResponse,  HttpResponseRedirect, QueryDict
from django.db import DatabaseError
from django.db import connection
from django.db import transaction
from django.db import models
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

from .utils import decorator_4xx
from .models import *
from .constants import *
# Create your views here.

class AddTransactionView(View):

	@csrf_exempt
	@decorator_4xx(['POST'],['wallet_id'])
	def post(request, wallet_id):
		response = {}
		token = request.POST['token']
		wallet_id = request.POST['wallet_id']
		amount = request.POST['amount']
		wallet = wallet.objects.get(pk = wallet_id)
		wallet.add_money(amount)
		response = json.dumps(response)
		return HttpResponse(response, content_type=RESPONSE_JSON_TYPE)

class RemoveTransactionView(View):

	@csrf_exempt
	@decorator_4xx(['POST'],['wallet_id'])
	def post(request, wallet_id):
		response = {}
		token = request.POST['token']
		amount = request.POST['amount']
		wallet_id = request.POST['wallet_id']
		wallet = wallet.objects.get(pk = wallet_id)
		wallet.withdraw_money(amount)
		response = json.dumps(response)
		return HttpResponse(response, content_type=RESPONSE_JSON_TYPE)




@csrf_exempt
def login(request):
	response = {}
	user = request.GET['username']
	password = request.GET['password']
	# authUser = User.objects.create_user(userId, emailId, token)
	user = auth.authenticate(username=user, password=password) 
	if user:
		token = Token.objects.get(wallet_user = user)
		response['token'] = token.token

	response = json.dumps(response)
	return HttpResponse(response, content_type=RESPONSE_JSON_TYPE)


# @decorator_4xx(['POST'],['wallet_id'])
# @csrf_exempt
# def add_transaction(request, wallet_id):
# 	token = request.POST['token']
#     response = json.dumps(response)
#     return HttpResponse(response, content_type=RESPONSE_JSON_TYPE)


# @decorator_4xx(['POST'],['wallet_id'])
# @csrf_exempt
# def withdraw_transaction(request, wallet_id):
# 	token = request.POST['token']
#     response = json.dumps(response)
#     return HttpResponse(response, content_type=RESPONSE_JSON_TYPE)
