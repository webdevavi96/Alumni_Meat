from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserRegistrationForm

# Create your views here.

def home(request): 
  return render(request, "index.html")
    
def about(request):
  return render(request, "master.html")
  
def blogs(request): 
  return render(request, "pages/blogs.html")
  
def gallery(request):
  return render(request, "pages/gallery.html")

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
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data['role'] == 'Admin':
                user.is_staff = True  # Admin users can access Django Admin
                user.is_superuser = True  # Grant superuser privileges
            user.save()
            login(request, user)  # Automatically log in the user
            return redirect('/')  # Redirect to homepage after registration
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'pages/register.html', {'form': form})