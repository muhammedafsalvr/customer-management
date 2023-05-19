from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=18)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
   
    

    def __str__(self):
        return self.first_name