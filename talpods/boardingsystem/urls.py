from django.urls import path
from .views import (
    BoardingPassSort
)

urlpatterns = [
    path('boarding_pass/sort', BoardingPassSort.as_view(), name='sort_boarding_passes'),
]
