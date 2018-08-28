from django.shortcuts import render

#Create your views here.

def index_call(request):
	return render(request, "index.html", {})


def reel_call(request):
	return render(request, "reel.html", {})


