from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note 
from .serializers import NoteSerializer
# Create your views here.

@api_view(['GET'])
def notes(request):
    all = Note.objects.all()
    serializer = NoteSerializer(all, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def note(request, pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)