from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'index.html', {'form' : form})


def success(request):
    return HttpResponse('successfully uploaded')


def display_hotel_images(request):

    if request.method == 'GET':
        Hotels = Hotel.objects.all() 
        context={
            'hotel_images' : Hotels
            }
        # getting all the objects of hotel.
        return render(request, 'display_hotel_images.html', context )