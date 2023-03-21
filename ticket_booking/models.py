from django.db import models

# Create your models here.
class Station(models.Model):
    station_code = models.IntegerField(primary_key=True)
    station_name = models.CharField('Station Name',max_length=50)
    # station_photo = models.ImageField(upload_to='media',blank=True)

    def __str__(self) :
        return self.station_name

class Train(models.Model):
    choice = (('UP','up'),('DOWN','down'))
    name = models.CharField('Train Name',max_length=30)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_from')
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='station_to')
    seat = models.IntegerField()
    start = models.TimeField()
    finish = models.TimeField()
    trip_type = models.CharField(choices=choice,max_length=30)
    date = models.DateField(auto_now=False,blank=True)

    def __str__(self) -> str:
        return self.name

class Trip(models.Model):
    from_station = models.CharField(max_length=30)
    to_station = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    date = models.DateField()
    seat = models.IntegerField()
    seat_class = models.CharField(max_length=10)
    fare = models.IntegerField(blank=True)
    payment = models.BooleanField(default=False,blank=True)

    def __str__(self) -> str:
        return f"{self.user}" + f"{self.date}"

class Ticket(models.Model):
    passenger = models.CharField(max_length=50)
    transport = models.CharField(max_length=50,null=True,blank=True)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    tickets = models.PositiveIntegerField(default=1)
    coach = models.CharField(max_length=30)
    cost = models.PositiveIntegerField(default=10)
    total_cost = models.PositiveIntegerField(default=10)

    def __str__(self):
        return str(self.passenger) + str(self.date)
    
    
