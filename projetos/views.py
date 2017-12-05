from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProjetoForm
from .models import Projeto
from projetos.plenarinho_crawler import *


class ProjetoList(ListView):
    model = Projeto
    paginate_by = 20


class ProjetoCreate(CreateView):
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('projetos:list')


class ProjetoDetail(DetailView):
    model = Projeto


class ProjetoUpdate(UpdateView):
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('projetos:list')


class ProjetoDelete(DeleteView):
    model = Projeto
    success_url = reverse_lazy('projetos:list')

def ProjetoCrawl(request):
    
    return HttpResponse(getProjetos())

