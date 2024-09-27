from django.urls import path
from leads.views import leads_list, lead_details, lead_create

app_name = 'leads'

urlpatterns = [
    path('', leads_list),
    path('<int:pk>/', lead_details),
    path('create/', lead_create)
]