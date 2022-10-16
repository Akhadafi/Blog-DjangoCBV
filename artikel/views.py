from django.views.generic import ListView, DetailView
from artikel.models import Artikel


class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/list.html"
    context_object_name = "artikel_list"
    ordering = ["-publish"]
    paginate_by = 3


class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = "artikel/detail.html"
    context_object_name = "artikel"
