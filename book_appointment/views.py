from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookAppointment
from .models import Doctors


# Create your views here.
def appointmentpage(request):
     #template=loader.get_template('book_appointment/Appointments.html')
     return render(request ,'book_appointment/Appointments.html' )


def selectslot(request):
     #doc=Doctors.objects.get(id=i)
     #return HttpResponse("<h3>"+str(doc.id)+"<br>"+doc.name+"<br>"+str(doc.img)+"</h3>")

     all_doctors = Doctors.objects.all()
     template=loader.get_template('book_appointment/Doctors.html')
     context={
          'all_doctors':all_doctors
     }
     return HttpResponse(template.render(context , request))

def booknow(request):
     template=loader.get_template('book_appointment/doc_appointment.html')
     return HttpResponse(template.render())
