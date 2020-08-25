from django.urls import path

from .views import StateListView

urlpatterns = [
    path("decision", StateListView.as_view(), name="eu-app"),
]