from django.urls import path
from .views import MultiStepFormView

urlpatterns = [
    path('employee-data/', MultiStepFormView.as_view(), name='multistep_data'),
]