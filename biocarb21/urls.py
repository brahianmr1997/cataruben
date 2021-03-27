from django.urls import path
from . import views
urlpatterns = [
    path("", views.registrate, name="registrate"),
    path("<str:nombre>/<str:email>/<str:telefono>/", views.registrate_2, name="registrate-2"),
    path("exito/<str:email>/", views.registrate_exito, name="registrate-exito"),
]