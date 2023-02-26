from django.db import models
from django.core.validators import MinValueValidator ,MaxValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 150 ,unique=True)
    original_price=models.FloatField()
    discount=models.IntegerField(
        default=0,
        validators=[MinValueValidator(0),MinValueValidator(100)]
                                 
            )
    
    

    def __str__(self):
        return self.name

   
