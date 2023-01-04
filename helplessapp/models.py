from django.db import models

# Create your models here.


class ContactForm(models.Model):
    first_name = models.CharField(max_length=250)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    message = models.TextField()

    def __str__(self):
         return self.first_name

 
    