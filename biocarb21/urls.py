from django.urls import path
from . import views
urlpatterns = [
    path("", views.registrate, name="registrate"),
    path("<int:user_id>/", views.registrate_2, name="registrate-2"),
    path("exito/<int:user_id>/", views.registrate_exito, name="registrate-exito"),
]