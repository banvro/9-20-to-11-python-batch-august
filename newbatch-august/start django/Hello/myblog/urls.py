from django.urls import path
from myblog import views

urlpatterns = [
   path("hlo", views.hlo),
   path("/", views.home),
   path("contact-us", views.contact),
   path("about-us", views.about),
]
