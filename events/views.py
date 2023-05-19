import json

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from events.forms import EventForm
from web.functions import generate_form_errors

# Create your views here.
@login_required(login_url='/users/login/')
def create_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            print(form.cleaned_data)
            form.save()
            
            
            response_data = {
                "status": "success",
                "title": "Success",
                "message": "Submitted successfully",
                "redirect": 'true',
                "redirect_url": reverse('web:index')
            }

            return HttpResponse(json.dumps(response_data), content_type='application/javascript')
        
        print(generate_form_errors(form))
        response_data = {
            "status": "false",
            "title": "Failed",
            "message": generate_form_errors(form),
        }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')

    else:

        form = EventForm()
        context = {
            "title": "Add New Events",
            "form": form
        }
        return render(request, "events/create.html", context=context)
        
        