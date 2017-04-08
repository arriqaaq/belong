# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import hashlib
import time
import random
import string

from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db import transaction
from django.db.models import Prefetch, Q
from django.db import InterfaceError, OperationalError, close_old_connections, connection, \
	IntegrityError, DatabaseError, DataError, transaction, reset_queries
from django.core.exceptions import ValidationError, FieldError, ObjectDoesNotExist

from django.utils.functional import cached_property

from .utils import unique_id_generator


# Create your models here.


class Wallet(models.Model):
	wallet_id = models.CharField(max_length=255, primary_key=True)
	amount = models.IntegerField(default=0)

	def add_money(self, amount):
		try:
			with transaction.atomic():
				Transactions.objects.add_transaction(self, amount, credit = True)
				return True, 'Transaction created successfully'
		except Exception, error_msg:
			print 101, error_msg
			return True, 'Transaction could not be created'

	def withdraw_money(self, kwargs):
		try:
			with transaction.atomic():
				Transactions.objects.add_transaction(self, amount, credit = False)
				return True, 'Transaction created successfully'
		except Exception, error_msg:
			print 102, error_msg
			return True, 'Transaction could not be created'


class TransactionsManager(models.Manager):
	''''''
	def add_transaction(self, wallet, amount, credit = False):

		txn_kwargs = {
			'happay_id' : unique_id_generator(),
			'amount' : amount,
			'wallet' : wallet,
		}

		if credit:
			txn_kwargs['txn_type'] = Transactions.CREDIT
		else:
			txn_kwargs['txn_type'] = Transactions.DEBIT

		new_txn = Transactions.objects.create(**kwargs)


class Transactions(models.Model):
	CREDIT = 'C-HPVCL'
	DEBIT = 'D-HPVCW'

	created_on = models.DateTimeField(auto_now_add=True, db_index=True)
	updated_on = models.DateTimeField(auto_now=True, db_index=True)
	tId = models.CharField(max_length=255, primary_key=True)
	wallet = models.ForeignKey(Wallet, null=True, blank=True)
	amount = models.IntegerField(default=0)
	txn_type = models.CharField(max_length=20)

	objects = TransactionsManager()


class Token(models.Model):
	token = models.CharField(max_length=255, primary_key=True)
	wallet_user = models.ForeignKey(User, null=True, blank=True)
