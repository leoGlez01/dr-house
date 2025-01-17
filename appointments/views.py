from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_time

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'appointments/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'appointments/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'appointments/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        
        if date and time:
            parsed_date = parse_date(date)
            parsed_time = parse_time(time)
            
            if parsed_date and parsed_time:
                messages.success(request, "Cita reservada con éxito.")
                return redirect('home')
            else:
                messages.error(request, "Fecha u hora no válidas.")
        else:
            messages.error(request, "Por favor, proporciona tanto la fecha como la hora.")
    
    messages.error(request, "Método de solicitud no válido.")
    return redirect('home')