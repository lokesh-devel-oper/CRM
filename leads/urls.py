from django.urls import path
from leads.views import leads_list, lead_details, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', leads_list, name="lead-list"),
    path('<int:pk>/', lead_details, name="lead-details"),
    path('create/', lead_create, name="create-lead"),
    path('<int:pk>/update/', lead_update, name="update-lead"),
    path('<int:pk>/delete/', lead_delete, name="delete-lead"),
]