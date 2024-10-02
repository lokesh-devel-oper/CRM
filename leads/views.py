from django.shortcuts import render, redirect
from django.http import HttpResponse
from leads.models import LEAD, Agent
from leads.forms import Leadform, LeadModelForm

def landing_page(request):
    return render(request, "landing.html")

def login_page(request):
    return render(request, "login.html")

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
    form = LeadModelForm()
    if request.method == "POST":
        print("Receiving Post Request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

def lead_update(request, pk):
    lead = LEAD.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        print("Receiving Post Request")
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)


def lead_delete(request, pk):
    lead = LEAD.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


# def lead_update(request, pk):
#     lead = LEAD.objects.get(id=pk)
#     form = Leadform()
#     if request.method == "POST":
#         print("Receiving Post Request")
#         form = Leadform(request.POST)
#         if form.is_valid():
#             print("The form is Valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)

# def lead_create(request):
    # form = Leadform()
    # if request.method == "POST":
    #     print("Receiving Post Request")
    #     form = Leadform(request.POST)
    #     if form.is_valid():
    #         print("The form is Valid")
    #         print(form.cleaned_data)
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = Agent.objects.first()
    #         LEAD.objects.create(
    #             first_name = first_name,
    #             last_name = last_name, 
    #             age = age,
    #             agent = agent
    #         )
    #         return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)