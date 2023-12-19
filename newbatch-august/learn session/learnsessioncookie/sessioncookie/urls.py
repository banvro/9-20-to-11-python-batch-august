from django.urls import path

from sessioncookie import views

urlpatterns = [
   path("set_session", views.set_session),
   path("get_sessionn", views.get_sessionn),
   path("dlt_session", views.dlt_session),

   path("set_cookie", views.set_cookies),
   path("get_cookies", views.get_cookies),
]