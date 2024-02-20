from django.urls import path
from .views import Board_Api, Board_detailed_Api

urlpatterns = [
    path('board/', Board_Api),
    path('board/<int:id>', Board_detailed_Api)
]
