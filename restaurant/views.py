from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "index.html")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]


class MenuItemView(generics.ListCreateAPIView):
    # With APIView class
    # def get(self, request):
    #     menu = models.Menu.objects.all()
    #     serializer = serializers.BookingSerializer(menu, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = serializers.MenuSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data}, status=201)

    # With ListCreateAPIView class
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer
