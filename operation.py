from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.safestring import mark_safe
import env, json, requests, pandas as pd, os
from datetime import date


class Authenticacion:
	def __init__(self,request):
		self.headers = {'Content-Type': 'application/json'}
		self.request = request

	def Login_Company(self, data):
		response = requests.request("POST", env.LOGIN, headers=self.headers, data=data)
		return json.loads(response.text)