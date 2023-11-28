from django.urls import path
from blog import views


urlpatterns = [
    path("", views.home),
    path("about", views.aboutus),
    path("contact", views.contactus),
    path("service", views.services),
]