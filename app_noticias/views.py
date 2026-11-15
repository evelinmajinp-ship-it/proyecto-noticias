
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Noticia



def inicio(request):

    busqueda = request.GET.get('buscar', '')

    noticias = Noticia.objects.all()

    if busqueda:
        noticias = noticias.filter(
            Q(titulo__icontains=busqueda) |
            Q(lugar__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    # Seleccionar la noticia más reciente
    noticia_destacada = noticias.first()

    # Excluir la noticia destacada de las demás
    otras_noticias = noticias

    if noticia_destacada:
        otras_noticias = noticias.exclude(pk=noticia_destacada.pk)

    # Mostrar seis noticias por página
    paginador = Paginator(otras_noticias, 6)

    numero_pagina = request.GET.get('page')
    otras_noticias = paginador.get_page(numero_pagina)

    return render(request, 'noticias/inicio.html', {
        'noticia_destacada': noticia_destacada,
        'noticias': otras_noticias,
        'busqueda': busqueda
    })



def detalle_noticia(request, pk):

    # Buscar la noticia por su identificador
    noticia = get_object_or_404(Noticia, pk=pk)

    return render(request, 'noticias/detalle.html', {
        'noticia': noticia
    })
