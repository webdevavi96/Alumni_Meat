from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# from .forms import CustomUserRegistrationForm

# Create your views here.

def home(request): 
  return render(request, "index.html")
    
def about(request):
  return render(request, "master.html")
  
def blogs(request): 
  return render(request, "pages/blogs.html")
  
def gallery(request):
  return render(request, "pages/gallery.html")

def contactUs(request):
  return render(request, "pages/contact-us.html")


@login_required
def userProfile(request):
  return render(request, "pages/profile.html")
  
@login_required
def events(request):
    # Check the user's type
    user = request.user
    if user.is_superuser:  # For admin users
        events = [
            {'id': 1, 'details': 'Welcome to Alumni Meet 2025', 'status': 'Upcoming', 'date_time': 'Monday 20 Jan 2PM'},
            {'id': 2, 'details': 'Technical Workshop by Experts', 'status': 'Ongoing', 'date_time': 'Tuesday 21 Jan 10AM'},
            {'id': 3, 'details': 'Cultural Program & Networking', 'status': 'Ended', 'date_time': 'Sunday 18 Jan 5PM'},
        ]
    elif user.groups.filter(name='Alumni').exists():  # For alumni users
        events = [
            {'id': 1, 'details': 'Welcome to Alumni Meet 2025', 'status': 'Ongoing', 'date_time': 'Monday 25 Jan 2PM'},
            {'id': 2, 'details': 'Technical Workshop by Experts', 'status': 'Upcoming', 'date_time': 'Tuesday 21 Jan 10AM'},
            {'id': 3, 'details': 'Cultural Program & Networking', 'status': 'Ended', 'date_time': 'Sunday 18 Jan 5PM'},
        ]
    else:  # For regular users
        events = [
            {'id': 1, 'details': 'Welcome to Alumni Meet 2025', 'status': 'Upcoming', 'date_time': 'Monday 30 Jan 2PM'},
            {'id': 2, 'details': 'Technical Workshop by Experts', 'status': 'Ended', 'date_time': 'Tuesday 21 Jan 10AM'},
            {'id': 3, 'details': 'Cultural Program & Networking', 'status': 'Ongoing', 'date_time': 'Sunday 18 Jan 5PM'},
        ]
    
    return render(request, 'pages/events.html', {'events': events})
    
def register(request):
  return render(request, 'pages/register.html')
  
def login(request):
  return render(request, 'pages/register.html')
  
def get_data(request):
  data = {
    "message": "Hello from django",
    "satus-code": 200,
    "status": "success"
  }
  return JsonResponse(data)
  
  
def varify_user(request):
  if request.method == 'POST':
    import json
    data = json.loads(request.body)
    
    email = data.get("email")
    password = data.get("password")
    
    user = authenticate(username=email,password=password)
    
    if user is not None:
      return JsonResponse({"status": "success", "message":"Logged In Successfully"})
    else:
      return JsonResponse({"status":"error", "message":"Failed"},statud=401)
      
  return JsonResponse({"status":"error","message":"Failed"},status=400)