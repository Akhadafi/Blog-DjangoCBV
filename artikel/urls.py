from django.urls import path, re_path
from django.views.generic import TemplateView
from artikel.views import ArtikelListView, ArtikelDetailView, ArtikelKategoriListView

urlpatterns = [
    path("", TemplateView.as_view(template_name="main.html"), name="home"),
    re_path(
        r"^artikel/kategori/(?P<kategori>[\w-]+)/(?P<page>\d+)$",
        ArtikelKategoriListView.as_view(),
        name="category",
    ),
    re_path(r"^artikel/(?P<page>\d+)$", ArtikelListView.as_view(), name="list"),
    path("artikel/<slug:slug>", ArtikelDetailView.as_view(), name="detail"),
]
