from django.db import models
from django.contrib.auth.models import AbstractUser
from pkg_resources import require


class User(AbstractUser):
    
    # Personal information
    username = models.CharField(
        ("username"),
        max_length=150,
        unique=True,
        help_text=
        ("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
         ),
        error_messages={
            "unique": ("A user with that username already exists."),
        },
        default="username")
    first_name = models.CharField(("first name"), max_length=150, blank=True)
    last_name = models.CharField(("last name"), max_length=150, blank=True)
    phone_number = models.CharField(max_length=20, default="")  
    info = models.CharField(max_length=2500, default="")
    medical_history = models.CharField(max_length=1000, default="")

    USERNAME_FIELD = "username"

    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    pdf = models.FileField(upload_to='pdf/%Y/%m/%d/', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return "%s %s - %s" % (self.first_name, self.last_name, self.username)

class Appointment(models.Model):
    user = models.ForeignKey(User, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    info = models.CharField(max_length=500, default="")
    diagnosis = models.CharField(max_length=1000, default="")
    
    def __str__(self):
        return "%s - %s - %s" % (self.user, self.date, self.time)
    
    