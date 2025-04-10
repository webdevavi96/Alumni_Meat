from django.contrib import admin
from django.urls import path
from AlumniApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("events/", views.events, name="events"),
    path("blogs/", views.blogs, name="blogs"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact-us/", views.contactUs, name="contact-us"),
    path("profile/", views.userProfile, name="profile"),
    path("accounts/login/", views.login, name="login"),
    path("register/", views.register, name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)