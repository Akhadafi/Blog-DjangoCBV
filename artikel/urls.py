from django.urls import path
from django.views.generic import TemplateView
from artikel.views import ArtikelListView

urlpatterns = [
    path("", TemplateView.as_view(template_name="main.html"), name="home"),
    path("artikel/", ArtikelListView.as_view(), name="list"),
]
