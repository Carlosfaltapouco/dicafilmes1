from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Dica

def index(request):
    dicas = Dica.objects.order_by('-date_da_dica').filter(publicada= True)
    
    
    dados = {
        'dicas' : dicas
    }
    return render(request, 'index.html', dados)


def dica(request, dica_id):
    dica = get_object_or_404(Dica, pk = dica_id)
    
    dica_a_exibir =  {
        'dica' : dica
    } 
    return render(request, 'dica.html', dica_a_exibir)
