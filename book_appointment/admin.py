from django.contrib import admin
from .models import BookAppointment
from .models import Doctors

# Register your models here.
admin.site.register(BookAppointment)
admin.site.register(Doctors)

