from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("savetodo", views.savethistodo, name = "ok"),
    path("deletethistodo/<int:myid>", views.deletethis),

    path("updatetodo/<int:myid>", views.updatetodo),

    path("updattodonow/<int:myid>", views.updatethisnow),
]
