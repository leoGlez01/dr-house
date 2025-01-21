from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_time
from .models import Appointment, Doctor, Patient
from .forms import CustomUserCreationForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'appointments/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'patient'
            user.save()
            Patient.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
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
                # Crear y guardar la cita
                Appointment.objects.create(
                    patient=request.user,
                    doctor=Doctor.objects.first(),  # Asigna un doctor adecuado aquí
                    appointment_date=parsed_date,
                    start_time=parsed_time,
                    end_time=(datetime.combine(parsed_date, parsed_time) + timedelta(hours=1)).time(),
                    status='confirmed'
                )
                messages.success(request, "Cita reservada con éxito.")
                return redirect('home')
            else:
                messages.error(request, "Fecha u hora no válidas.")
        else:
            messages.error(request, "Por favor, proporciona tanto la fecha como la hora.")
    
    messages.error(request, "Método de solicitud no válido.")
    return redirect('home')


@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})