from django.urls import path
from hlo import views

urlpatterns = [
    path("get-data", views.getingdata),
    path("save-data", views.savethisdata),
    path("delete-data/<int:id>", views.detethiddata),
    path("update-data/<int:id>", views.updatethisdata),
]
