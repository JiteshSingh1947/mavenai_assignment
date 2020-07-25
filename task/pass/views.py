from django.shortcuts import render
from .import models
from .forms import RegisterForm
from rest_framework import viewsets
from .serializers import profileSerializer
# Create your views here.

def register(request):

	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = RegisterForm()
    
	return render(request,'register.html',{'form':form})



def detail(request):
	dashboard=models.profile.objects.all()
	return render (request,'detail.html',{'dashboard':dashboard})


class proView(viewsets.ModelViewSet):
	queryset = models.profile.objects.all()
	serializer_class = profileSerializer		