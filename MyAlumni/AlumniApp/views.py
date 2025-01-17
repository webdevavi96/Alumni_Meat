from django.shortcuts import render

# Create your views here.

def home(request): 
  return render(request, "index.html")
    
def about(request):
  return render(request, "master.html")
  
def events(request):
    events = [
        {'id': 1, 'details': 'Welcome to Alumni Meet 2025', 'status': 'Upcoming', 'date_time': 'Monday 20 Jan 2PM'},
        {'id': 2, 'details': 'Technical Workshop by Experts', 'status': 'Ongoing', 'date_time': 'Tuesday 21 Jan 10AM'},
        {'id': 3, 'details': 'Cultural Program & Networking', 'status': 'Ended', 'date_time': 'Sunday 18 Jan 5PM'},
    ]
    return render(request, 'static/pages/events.html', {'events': events})
