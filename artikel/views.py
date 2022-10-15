from django.views.generic import ListView
from artikel.models import Artikel


class ArtikelListView(ListView):
    model = Artikel
    template_name = "artikel/list.html"
    context_object_name = "artikel_list"
