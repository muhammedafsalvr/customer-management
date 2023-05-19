from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import HttpResponse

from events.models import Event
from users.models import Customer


def index(request):
    events = Event.objects.filter(is_deleted=False,single_time=True)
    customers = Customer.objects.all()

    context = {
        "title": "Home Page",
        "events": events,
        "customers": customers,

    }
    return render(request, 'web/index.html', context=context)
