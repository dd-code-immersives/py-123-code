from django.shortcuts import render, redirect
from django.db import models
from .models import UserDetails
from django.template import loader
from django.http import HttpResponse
from django.forms import modelformset_factory

from .forms import UserModelForm
# Create your views here.


def userDetails(request):

	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			u = form.save()
			users = UserDetails.objects.all()
			return render(request, "display.html", {'users': users})
			#return redirect("/display")
	else: 
		form_class = UserModelForm
		return render(request, 'userdetails.html', {'form':form_class})
