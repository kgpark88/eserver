from django.urls import path

from energy import views

urlpatterns = [
    path('usage', views.energy_usage, name='energy'),
]
