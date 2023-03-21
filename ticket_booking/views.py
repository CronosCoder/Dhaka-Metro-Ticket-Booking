from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Station,Train,Trip,Ticket

# Create your views here.
@login_required(login_url='login')
def search_page(request):
    station = Station.objects.all()
    if request.method == "POST":
        from_station = request.POST['from']
        to_station = request.POST['to']
        date = request.POST['date']
        seat = int(request.POST['seat'])
        seat_coach = request.POST['class']
        age = request.POST['age']
        user = request.user.username

        from_code = Station.objects.get(station_name = from_station).station_code
        to_code = Station.objects.get(station_name = to_station).station_code
        distance = abs(from_code-to_code)
        fare = 0
        if seat_coach == "AC":
            fare = 20 * distance * seat
        elif seat_coach == "Non AC":
            fare = 15 * distance * seat
        else:
            fare = 10 * distance * seat

        if fare < 10:
            fare = 10
        
        trip_type = 'up'
        if from_code < to_code :
            trip_type = 'up'
        else:
            trip_type = 'down'
        
        trip = Trip(from_station=from_station,to_station=to_station,user=user,date=date,seat=seat,seat_class=seat_coach,fare=fare,payment=False)
        trip.save()
        available_trains = Train.objects.all().filter(trip_type=trip_type,date=date)
        return render(request,'book/book.html',{'trip':trip,'trains':available_trains})
    return render(request,'search/search.html',{'stations':station})

@login_required(login_url='login')
def book_page(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        print(data)
    return render(request,'book/book.html')

@login_required(login_url='login')
def book_train(request,id):
    train = get_object_or_404(Train,pk=id)
    user = request.user
    trip = Trip.objects.all().filter(user=user.username,date=train.date).order_by('-id')[0]

    passenger = user.first_name +" "+ user.last_name
    transport = train.name
    source = trip.from_station
    destination = trip.to_station
    date = train.date
    time = train.start
    tickets = trip.seat
    coach = trip.seat_class
    cost = trip.fare
    total_cost = cost + 40
    
    train.seat = train.seat - tickets
    train.save()
    trip.payment = True
    trip.save()

    ticket = Ticket(passenger=passenger,transport=transport,source=source,destination=destination,date=date,time=time,tickets=tickets,coach=coach,cost=cost,total_cost=total_cost)
    ticket.save()

    try:
        subject = "Ticket booking confirmation by Dhaka Metro"
        message = f"Hey {passenger}, You have successfully booked you ticket. Please pay the bill firstly to get your ticket."
        send_mail(subject,message,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)
    except:
        pass
    
    return render(request,'payment/payment.html',{'ticket':ticket})

@login_required(login_url='login')
def train_info(request):
    trains = Train.objects.all()
    return render(request,'train_info/train_info.html',{'all_train':trains})

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

@login_required(login_url='login')
def show_routes(request):
    return render(request,'routes/routes.html')