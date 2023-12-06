from django.urls import path
from blog import views
 

urlpatterns = [
    path("", views.home, name = "home"),
    path("savedata", views.suaveinfo, name = "suaveinfo"),
    path("showdata", views.showthisdta, name = "show"),

    path("deletethis/<int:myid>", views.deletethis, name = "dlt"),
]