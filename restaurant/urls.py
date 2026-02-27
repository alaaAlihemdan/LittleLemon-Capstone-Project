# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('menu/', views.MenuItemsView.as_view()),
#     path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
#     path('booking/', views.BookingView.as_view()),
# ]

# restaurant/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('reservations/', views.reservations, name='reservations'),
    
    path('menu/', views.menu, name='menu'), 
    path('api/menu/', views.MenuItemsView.as_view()), 
    
   # بدلاً من SingleMenuItemView سنستخدم الدالة الجديدة
    path('menu/<int:pk>', views.display_menu_item, name='menu_item'),
    
    path('booking/', views.BookingView.as_view(), name='booking_api'),
    path('bookings/', views.bookings, name='bookings'),
]