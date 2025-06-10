from django.db import models
from django.conf import settings

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = (
        ('GP', 'General Practitioner'),
        ('CARD', 'Cardiologist'),
        ('NEURO', 'Neurologist'),
        ('PED', 'Pediatrician'),
        ('DERM', 'Dermatologist'),
        ('ORTHO', 'Orthopedist'),
        ('PSYCH', 'Psychiatrist'),
        ('OTHER', 'Other'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=5, choices=SPECIALIZATION_CHOICES)
    license_number = models.CharField(max_length=50, unique=True)
    years_of_experience = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"Dr. {self.first_name} {self.last_name}"
