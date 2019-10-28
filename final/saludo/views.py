from django.shortcuts import render, redirect
from .models import Lista_tareas
from .forms import TareasForm


def tarea(request, tarea_id=None):
    instancia = None    
    if tarea_id:
        instancia = Lista_tareas.objects.get(id=tarea_id)
    form = TareasForm(instance=instancia)
    if request.method == 'POST':
        form = TareasForm(request.POST,instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            tareas = form.save(commit=False)
            tareas.save()
            return redirect ('/')       
    return render(request, 'form.html', {'form': form})

def lista(request):
    tareas = Lista_tareas.objects.all() 
    return render(request, 'lista.html', {'Lista_tareas': tareas})




