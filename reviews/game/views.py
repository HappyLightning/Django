from django.shortcuts import render
from .models import Jogo


# Create your views here.
def homepage(request):
    jogos = Jogo.objects.all()
    return render(request, 'games/home.html', {'jogos': jogos})