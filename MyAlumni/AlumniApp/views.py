from django.shortcuts import render

# Create your views here.

def landing(request): 
  return render(request, "index.html")
    
def homepage(request):
  return render(request, "master.html")