from django.urls import path
from basic import views

urlpatterns = [
    path("", views.main),
    path("xyz", views.xyz),
    ]
