from django.shortcuts import render
from bigbox.models import Activity, Box,Prodcut,Category
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.


def box(request):
    # Todos los objetos  de la class Box, lo guardamos dentro de la variable.
    boxs = Box.objects.all()
    # Luego mostramos los datos en box.html
    
    return render(request, "box.html", {"boxs": boxs})

def infobox(request, category_id):
    # filtra la box que reciba en el parametro categoria_id
    boxs = Box.objects.filter(id=category_id )
    # Muestra las primeras cinco actividades
    activities= Activity.objects.all()[:5]
    
    return render(request, "infobox.html", {"boxs": boxs,"activities":activities})

def activity(request):
    # Muestra todas las actividades /incluye paginador   
    activ = Activity.objects.filter.all(boxs)
    actividades= Activity.objects.all()
    paginator = Paginator(actividades,20)
    
    page = request.GET.get("page",1)
    activitividades_page = paginator.get_page(page)           
    
    return render(request, "activity.html",{"actividades":actividades,"actividades_page":actividades_page,"actividades_list":actividades_list,"activ":activ })
