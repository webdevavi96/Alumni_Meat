from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


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
  if request.method == 'POST': 
    user_Email = request.POST.get('login_email')
    user_Password = request.POST.get('login_password')
    
    if Users.objects.filter(user_Email=user_Email).exists(): 
      user = authenticate(regular, user_Email=user_Email, user_Password=user_Password)
      
      if user is not none: 
        login(request, user)
        return redirect('home')
        
      else:
        message.error(reuest, "Email or Password didn’t matched!....")
    else:
      message.error(reuest, "User dose not exists!...")
  return render(request, 'pages/register.html')
  



def new_user(request):
    if request.method == 'POST':
        full_name = request.POST.get("fullname")
        email = request.POST.get("email")
        user_type = request.POST.get("user_type")
        password = request.POST.get("password")

        if not all([full_name, email, user_type, password]):
            return redirect('register')

        if Users.objects.filter(email=email).exists():
            return redirect('register')

        if user_type.upper() == "STUDENT":
            branch = request.POST.get("branch")
            enrollment_number = request.POST.get("enrollment")
            year = request.POST.get("year")

            if not all([branch, enrollment_number, year]):
                return redirect('register')

            Users.objects.create(
                full_name=full_name,
                email=email,
                user_type=user_type,
                branch=branch,
                enrollment_number=enrollment_number,
                year=year,
                password=make_password(password),
            )
            return redirect('login')

        Users.objects.create(
            full_name=full_name,
            email=email,
            user_type=user_type,
            password=make_password(password),
        )
        return redirect('login')

    return render(request, 'register.html')