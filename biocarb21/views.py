from django.shortcuts import render, redirect
from .models import Userbc21
from .forms import Userbc21Form1, Userbc21Form2

def registrate(request):
    if request.method == "POST":
        form = Userbc21Form1(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('registrate-2', user.id)
    else:
        form = Userbc21Form1()
    context = {'form': form}
    return render(request, 'biocarb21\\registrate.html', context)

def registrate_2(request, user_id):
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




