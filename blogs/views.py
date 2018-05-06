from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def blogpost(request):
    """ Pagina do blog """
    blogposts = BlogPost.objects.all()

    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = BlogPostForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogpost'))



    context = {'blogposts': blogposts, 'form': form}
    return render(request, 'blogs/blogpost.html', context)

def new_area(request):
    """ Adiciona um novo assunto """
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = BlogPostForm()
    else:
        # Dados de POST submetidos; processa os dados
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blogpost'))
    context = {'form': form}
    return render(request, 'blogs/new_area.html', context)


