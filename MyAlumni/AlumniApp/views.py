from django.shortcuts import render
from django.http import JsonResponse
import json
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
  



def verify_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            # Check if user exists
            user = User.objects.filter(user_Email=email).first()
            
            if user:
                # Check password
                if check_password(password, user.user_Password):
                    # Redirect to home on success
                    return JsonResponse({"status": "success", "message": "Login Successfull."}, status=201)
                else:
                    return JsonResponse({"status": "error", "message": "Invalid password!"}, status=401)
            else:
                return JsonResponse({"status": "error", "message": "User not found!"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)

    return JsonResponse({"status": "error", "message": "Invalid request method!"}, status=400)
  


def new_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract Common Fields
            full_name = data.get("fullname")
            user_Email = data.get("email")
            user_type = data.get("user_type")
            user_Password = data.get("password")

            # Check if user already exists
            if User.objects.filter(user_Email=user_Email).exists():
                return JsonResponse({"status": "error", "message": "User already exists!"}, status=400)

            # Handle Student Specific Data
            if user_type == "STUDENT":
                branch = data.get("branch")
                enrollment_Number = data.get("enrollment")
                year = data.get("year")

                user = User.objects.create(
                    full_name=full_name,
                    user_Email=user_Email,
                    user_type=user_type,
                    branch=branch,
                    enrollment_Number=enrollment_Number,
                    year=year,
                    user_Password=user_Password,
                )
                return JsonResponse({"status": "success", "message": "Student account created successfully!"}, status=201)

            # For Admin or Alumni
            else:
                user = User.objects.create(
                    full_name=full_name,
                    user_Email=user_Email,
                    user_type=user_type,
                    user_Password=user_Password,
                )
                return JsonResponse({"status": "success", "message": "Account created successfully!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)