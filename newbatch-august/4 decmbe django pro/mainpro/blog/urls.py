from django.urls import path
from blog import views
 

urlpatterns = [
    path("", views.home, name = "home"),
    path("savedata", views.suaveinfo, name = "suaveinfo"),
    path("showdata", views.showthisdta, name = "show"),

    path("updatedata/<int:x>", views.updatedata, name = "update"),

    path("deletethis/<int:myid>", views.deletethis, name = "dlt"),

    path("updatenow/<int:id>", views.updatenow)
]