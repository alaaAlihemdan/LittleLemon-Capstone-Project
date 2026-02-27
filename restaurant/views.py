from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from .forms import BookingForm # ستحتاج لإنشاء ملف forms.py أولاً
from django.core import serializers
from django.http import JsonResponse
from datetime import datetime
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt

# الصفحات العادية (HTML)
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def book(request):
#     return render(request, 'book.html')

def reservations(request):
    return render(request, 'bookings.html')

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu_items})

# الـ API (التي تسببت في الخطأ لأنها لم تكن مطابقة للأسماء في urls)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
 

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

# هذه الدالة مهمة جداً لـ JavaScript لجلب المواعيد
def bookings(request):
    date = request.GET.get('date')
    bookings_data = Booking.objects.filter(reservation_date=date)
    data = serializers.serialize('json', bookings_data)
    return JsonResponse(data, safe=False)

def menu(request):
    menu_data = Menu.objects.all()
    # إذا كان القالب يتوقع كلمة 'menu' كـ QuerySet
    return render(request, 'menu.html', {'menu': menu_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item})
