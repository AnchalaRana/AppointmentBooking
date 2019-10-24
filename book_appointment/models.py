from django.db import models

# Create your models here.
class BookAppointment(models.Model):
    name = models.TextField()
    relation = models.TextField(blank=True , null=True)
    mobile = models.TextField(max_length=10)
    address = models.TextField()
    dob = models.DateTimeField()

    def __str__(self):
        return self.name + '-' +self.mobile

class Doctors(models.Model):
      name = models.CharField(max_length=255)
      specialist=models.CharField(max_length=255)
      img=models.ImageField(upload_to='images/')

      def __str__(self):
        return self.name + '-' +self.specialist

