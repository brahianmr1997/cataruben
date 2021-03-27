from django.shortcuts import render, redirect
from .models import Userbc21
from .forms import Userbc21Form1, Userbc21Form2



def registrate(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST['telefono']
        return redirect('registrate-2', nombre, email, telefono)
    return render(request, 'biocarb21\\registrate.html')

def registrate_2(request, nombre, email, telefono):
    user = Userbc21.objects.get(id = user_id)
    if request.method == "POST":
        form = Userbc21Form2(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('registrate-exito', user.id)
    else:
        form = Userbc21Form2(instance = user)
    context = {'form' : form}
    return render(request, 'biocarb21\\registrate-2.html', context)

def registrate_exito(request, user_id):
    user = Userbc21.objects.get(id = user_id)
    return render(request, 'biocarb21\\registrate-exito.html')#, context




