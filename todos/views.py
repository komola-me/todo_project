from django.shortcuts import render
from rest_framework import generics

from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer