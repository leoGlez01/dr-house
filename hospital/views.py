from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_time
from .models import Appointment, Doctor, Patient, User
from .forms import CustomUserCreationForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    doctors = Doctor.objects.all()
    return render(request, 'appointments/home.html', {'doctors': doctors})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role')
            if user.role == 'doctor':
                user.is_staff = True
                user.is_superuser = True
            user.save()
            if user.role == 'patient':
                Patient.objects.create(user=user)
            elif user.role == 'doctor':
                Doctor.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            if user.role == 'doctor':
                return redirect('doctor_panel')
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
            if user.is_staff or user.is_superuser:
                return redirect('doctor_panel')
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
        doctor_id = request.POST.get('doctor')
        
        if date and time and doctor_id:
            parsed_date = parse_date(date)
            parsed_time = parse_time(time)
            doctor = Doctor.objects.get(id=doctor_id)
            
            if parsed_date and parsed_time:
                # Crear y guardar la cita
                Appointment.objects.create(
                    patient=request.user,
                    doctor=doctor,
                    appointment_date=parsed_date,
                    start_time=parsed_time,
                    end_time=(datetime.combine(parsed_date, parsed_time) + timedelta(hours=1)).time(),
                    status='pending'
                )
                messages.success(request, "Cita reservada con éxito.")
                return redirect('home')
            else:
                messages.error(request, "Fecha u hora no válidas.")
        else:
            messages.error(request, "Por favor, proporciona todos los datos requeridos.")
    
    messages.error(request, "Método de solicitud no válido.")
    return redirect('home')

@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})

@login_required
def doctor_panel(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('home')
    appointments = Appointment.objects.filter(doctor__user=request.user, status='pending')
    return render(request, 'appointments/doctor_panel.html', {'appointments': appointments})

@login_required
def update_appointment_status(request, appointment_id, status):
    if not (request.user.is_staff or request.user.is_superuser):
        return redirect('home')
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = status
    appointment.save()
    return redirect('doctor_panel')