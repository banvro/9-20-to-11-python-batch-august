from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("savetodo", views.savethistodo, name = "ok"),
]
