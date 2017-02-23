from django.shortcuts import render

# Create your views here.

# class MyView(View):
# 	def get(self,request,*args,**kwargs):
# 		return HttpResponse("Hello, Word")	
from django.views.generic import ListView
from contacts.models import Contact 

class ListContactView(ListView):
	model=Contact
	template_name='contact_list.html'
