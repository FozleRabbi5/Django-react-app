from django.urls import path 
from . import views


urlpatterns = [
    path('',views.notes, name='notes' ),
    path('note/<str:pk>', views.note, name='note'),
]
