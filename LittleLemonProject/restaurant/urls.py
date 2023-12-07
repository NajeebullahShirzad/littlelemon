from django.urls import path
from . import views
from django.urls import path
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemview.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
]