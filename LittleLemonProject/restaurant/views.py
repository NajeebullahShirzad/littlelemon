from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MenuSerializer, BookingSerialzer, UserSerializer
from .models import Menu, Booking
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse, response
from django.views.generic import View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import request, response


# Create your views here.

class MenuView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
class SingleMenuItemview(View):
    model = Menu
    serializer_class = MenuSerializer
    def get(self, request, pk):
        menu_item = get_object_or_404(Menu, pk=pk)
        data = {
            'title':menu_item.title,
            'price':menu_item.price,
            'inventory':menu_item.inventory,
            
        }
        return JsonResponse(data)
    
    def put(self, request,pk):
        menu_item = get_object_or_404(Menu, pk=pk)
        data = {'success': False}
        try:
            menu_item.title = request.POST.get('title')
            menu_item.inventory = request.POST.get('inventory')
            menu_item.price = request.POST.get('price')
            menu_item.save()
            data['success'] = True
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def delete(self, request, pk):
        menu_item = get_object_or_404(Menu, pk=pk)
        data = {'success': False}
        try:
            menu_item.delete()
            data['success'] = True
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerialzer
    permission_classes = [IsAuthenticated]
    
    

#class UserViewSet(viewsets.ModelViewSet):
 #   queryset = User.objects.all()
  #  serializer_class = UserSerializer
   # permission_classes = [permissions.IsAuthenticated]
#in views.py


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return response({"message":"This view is protected"})