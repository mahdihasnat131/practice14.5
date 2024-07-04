from django.db import models



# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    phone_no=models.CharField(max_length=12)
    email=models.EmailField()
    date_time_field=models.DateTimeField()
    date_field=models.DateField()
    boolean_field=models.BooleanField()
    duration_field=models.DurationField()
    decimal_field=models.DecimalField(max_digits=7,decimal_places=4)
    binary_field=models.BinaryField()
    

    
    def __str__(self):
        return self.name