from django.db import models
from login.models import Customer,RoomManager
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    message=models.TextField(max_length=2000)
    def __str__(self):
        return self.name
class Rooms(models.Model):
    manager=models.ForeignKey(RoomManager, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5)
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=1000.00)
    no_of_days_advance=models.IntegerField()
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    status=models.BooleanField(default=False)
class RoomImage(models.Model):
    room=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None)
class Booking(models.Model):
    room_no=models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_day=models.DateField(auto_now=False, auto_now_add=False)
    end_day=models.DateField(auto_now=False, auto_now_add=False)
    amount=models.FloatField()


