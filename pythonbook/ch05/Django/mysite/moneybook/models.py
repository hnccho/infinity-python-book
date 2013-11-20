from django.db import models

class Transaction(models.Model):
    value = models.DecimalField(decimal_places=0, max_digits=10)
    name = models.CharField(max_length=20)
    date = models.DateField()
    
    def  __str__(self):
        return self.name
