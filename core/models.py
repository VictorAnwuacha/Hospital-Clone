from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    available_days = models.CharField(max_length=100)  # e.g., "Monday, Wednesday, Friday"
    start_time = models.TimeField()  # e.g., doctor's start time each day
    end_time = models.TimeField()    # e.g., doctor's end time each day
    image = models.ImageField(upload_to='images/doctors')

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} - {self.specialty}"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment on {self.appointment_date} at {self.appointment_time} with {self.doctor}"


class Notification(models.Model):
    recipient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient} at {self.created_at}"
