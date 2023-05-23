from datetime import date, datetime, timedelta

from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse
from django.contrib.auth.models import User

from events.models import Event
from users.models import Customer


def index(request):
    if request.method == 'POST':
        sort_date = request.POST.get('sort')  
        customers = request.POST.getlist('customer')  

        events = Event.objects.all()
        if customers:
            customer_users = User.objects.filter(username__in=customers)
            customers = Customer.objects.filter(user__in=customer_users)
            events = events.filter(customer__in=customers)
        
        if sort_date == 'today':
            events = events.filter(event_date= datetime.today())
            print(datetime.today(),"today")
        elif sort_date == 'week':
            start_of_week = date.today() - timedelta(days=date.today().weekday())
            print(date.today(),"today")
            print(timedelta(days=date.today().weekday()),"timedelta")
            end_of_week = start_of_week + timedelta(days=6)
            print(start_of_week,end_of_week,"week")
            events = events.filter(event_date__range=[start_of_week, end_of_week])
        elif sort_date == 'month':
            start_of_month = date.today().replace(day=1)
            end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            events = events.filter(event_date__range=[start_of_month, end_of_month])

        customers = Customer.objects.all()
        context = {
            "title": "Home Page",
            "events": events,
            "customers": customers,
        }

        return render(request, 'web/index.html', context)
    else:
        events = Event.objects.filter(is_deleted=False, single_time=True)
        customers = Customer.objects.all()

        context = {
            "title": "Home Page",
            "events": events,
            "customers": customers,

        }
        return render(request, 'web/index.html', context=context)
