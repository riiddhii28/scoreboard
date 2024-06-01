from django.shortcuts import render
#from django.http import HttpResponse





# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def adminpage(request):
    return render(request, 'adminpage.html')

def football(request):
    return render(request, 'football.html')

def tt(request):
    return render(request, 'tt.html')

def fdetails(request):
    return render(request, 'fdetails.html')

def fresults(request):
    return render(request, 'fresults.html')


def ttdetails(request):
    return render(request, 'ttdetails.html')


def ttresults(request):
    return render(request, 'ttresults.html')

def fmain(request):
    return render(request, 'fmain.html')

def ttmain(request):
    return render(request, 'ttmain.html')

def cricket(request):
    return render(request, 'cricket.html')

def cricketmain(request):
    return render(request, 'cricketmain.html')






