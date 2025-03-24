from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


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
    "status-code": 200,
    "status": "success"
  }
  return JsonResponse(data)
  


@csrf_exempt
def varify_user(request):
  if request.method == 'POST':
    import json
    data = json.loads(request.body)
    
    email = data.get("email")
    password = data.get("password")
    
    user = authenticate(user_Email=email, user_Password=password)
    
    if user is not None:
      return JsonResponse({"status": "success", "message":"Logged In Successfully"})
    else:
      return JsonResponse({"status":"error", "message":"User not found!"},status=401)
      
  return JsonResponse({"status":"error","message":"Invalid Request! "},status=400)
  


@csrf_exempt
def new_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Common Fields
            full_name = data.get("fullname")
            user_Email = data.get("email")
            user_type = data.get("user_type")
            user_Password = data.get("password")
            
            
            # Check if user already exists
            if User.objects.filter(user_Email=user_Email).exists():
                return JsonResponse({"status": "error", "message": "User already exists!"}, status=400)
            
            # Handle Student Specific Data
            if user_type == "Student":
                branch = data.get("branch")
                enrollment_Number = data.get("enrollment")
                year = data.get("year")
                
                
                # Create Student User
                user = User.objects.create(
                    full_name=full_name,
                    branch=branch,
                    user_Email=user_Email,
                    year=year,
                    enrollment_Number=enrollment_Number,
                    user_type=user_type,
                    password=user_Password
                )
                return JsonResponse({"status": "success", "message": "Student account created successfully!"}, status=201)
            
            # Create Non-Student User
            else:
                user = User.objects.create(
                    full_name=full_name,
                    user_Email=user_Email,
                    user_type=user_type,
                    password=user_Password
                )
                return JsonResponse({"status": "success", "message": "Account created successfully!"}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
    
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
  

