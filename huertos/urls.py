from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:huerto_id>", views.Huerto, name="huerto")
]