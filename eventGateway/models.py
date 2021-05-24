from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defualt.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Student'



class Events(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=50)
    max_participants = models.IntegerField()
    up = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='Event_pics')
    VALUES = (
        ("pending", "pending"),
        ("rejected", "rejected"),
        ("approved", "approved")
    )
    status = models.CharField(max_length=10, choices=VALUES, default="pending")

    def __str__(self):
        return self.title


class EventRegisteration(models.Model):
    event = models.ForeignKey(Events, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    open = models.BooleanField(default=True)
    participants = models.AutoField(primary_key=True)
