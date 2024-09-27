from django.shortcuts import render, redirect
from django.http import HttpResponse
from leads.models import LEAD, Agent
from leads.forms import Leadform

# Create your views here.
def leads_list(request):

    leads = LEAD.objects.all()
    context = {
        'leads': leads
    }

    return render(request, 'leads/leads_list.html', context=context)

def lead_details(request, pk):
    lead = LEAD.objects.get(id=pk)
    context = {
        'lead': lead
    }

    return render(request, "leads/lead_details.html", context)

def lead_create(request):
    form = Leadform()
    if request.method == "POST":
        print("Receiving Post Request")
        form = Leadform(request.POST)
        if form.is_valid():
            print("The form is Valid")
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            LEAD.objects.create(
                first_name = first_name,
                last_name = last_name, 
                age = age,
                agent = agent
            )
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
