from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Intro(models.Model):
    name = models.CharField(max_length = 50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(max_length = 40)
    about = models.TextField()

    def __str__(self):
            return self.name