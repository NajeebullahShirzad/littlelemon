from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer, BookingSerialzer, UserSerializer
from .models import Menu, Booking, User
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerialzer
    
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
