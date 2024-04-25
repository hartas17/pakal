from django.shortcuts import render

from .models import Huerto, Foto


# Create your views here.
def index(request):
    return render(request, "huertos/index.html", {
        "huertos": Huerto.objects.all(),
        "fotos": Foto.objects.all()
    })

def huerto(request, huerto_id):
    huerto = Huerto.objects.get(pk=huerto_id)
    return render(request, "huertos/huerto.html", {
        "huerto": huerto
    })