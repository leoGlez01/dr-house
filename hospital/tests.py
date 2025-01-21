from django.test import TestCase
from django.urls import reverse
from .models import Appointment
from django.contrib.auth.models import User

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.appointment = Appointment.objects.create(
            user=self.user,
            date='2023-10-01',
            time='10:00',
            reason='Checkup'
        )

    def test_appointment_creation(self):
        self.assertEqual(self.appointment.user.username, 'testuser')
        self.assertEqual(str(self.appointment.date), '2023-10-01')
        self.assertEqual(self.appointment.time, '10:00')
        self.assertEqual(self.appointment.reason, 'Checkup')

class AppointmentViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_appointment_list_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('hospital:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hospital/home.html')