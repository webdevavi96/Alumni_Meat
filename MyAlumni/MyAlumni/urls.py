"""
URL configuration for MyAlumni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from AlumniApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("events/", views.events, name = "events"),
    path("blogs/", views.blogs, name = "blogs"),
    path("register/", views.register, name = "register"),
    path("gallery/", views.gallery, name = "gallery"),
    path("contact-us", views.contactUs, name = "contact-us"),
    path("profile/", views.userProfile, name = "profile"),
    path("register/", views.register, name = "register"),
    path("accounts/login/", views.login, name = "login"),
    path("api/data/", views.get_data, name = "get_data"),
    path("api/varify_user/", views.varify_user, name = "varify_user"),
    path('api/register_user/', views.os.path.join(BASE_DIR,'static'),
	, name = "register_user"),
] + static(settings.MEDIA_URL, document_root.settings.MEDIA_ROOT)
