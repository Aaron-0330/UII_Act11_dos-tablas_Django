from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario_pasajero, Tarjeta
from .forms import UsuarioPasajeroForm, TarjetaForm
from django.forms import inlineformset_factory # Para gestionar tarjetas en el mismo formulario

# Home: Listar todos los pasajeros
def listar_pasajeros(request):
    pasajeros = Usuario_pasajero.objects.all()
    return render(request, 'listar_pasajeros.html', {'pasajeros': pasajeros})

# Detalle de un pasajero y sus tarjetas
def detalle_pasajero(request, id_usuario):
    pasajero = get_object_or_404(Usuario_pasajero, id_usuario=id_usuario)
    return render(request, 'detalle_pasajero.html', {'pasajero': pasajero})

# Crear un nuevo pasajero
def crear_pasajero(request):
    if request.method == 'POST':
        form = UsuarioPasajeroForm(request.POST, request.FILES)
        if form.is_valid():
            pasajero = form.save()
            return redirect('app_uber:detalle_pasajero', id_usuario=pasajero.id_usuario)
    else:
        form = UsuarioPasajeroForm()
    return render(request, 'formulario_pasajero.html', {'form': form, 'titulo': 'Registrar Nuevo Pasajero'})

# Editar un pasajero y sus tarjetas
def editar_pasajero(request, id_usuario):
    pasajero = get_object_or_404(Usuario_pasajero, id_usuario=id_usuario)
    # Permite añadir o modificar hasta 3 tarjetas por usuario en el mismo formulario
    TarjetaFormSet = inlineformset_factory(Usuario_pasajero, Tarjeta, form=TarjetaForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = UsuarioPasajeroForm(request.POST, request.FILES, instance=pasajero)
        formset = TarjetaFormSet(request.POST, request.FILES, instance=pasajero)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('app_uber:detalle_pasajero', id_usuario=pasajero.id_usuario)
    else:
        form = UsuarioPasajeroForm(instance=pasajero)
        formset = TarjetaFormSet(instance=pasajero)
    
    return render(request, 'formulario_pasajero.html', {
        'form': form, 
        'formset': formset, 
        'titulo': f'Editar Pasajero: {pasajero.nombre}'
    })

# Borrar un pasajero
def borrar_pasajero(request, id_usuario):
    pasajero = get_object_or_404(Usuario_pasajero, id_usuario=id_usuario)
    if request.method == 'POST':
        pasajero.delete()
        return redirect('app_uber:listar_pasajeros')
    return render(request, 'confirmar_borrar_pasajero.html', {'pasajero': pasajero})