from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title ', 'price', 'inventory']
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
        
class BookingSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['ID', 'Name', 'No_of_guests', 'BookingDate']
    
    