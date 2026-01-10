from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('search-booking/', views.search_booking, name='search_booking'),
    path('availability/', views.get_availability, name='get_availability'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    
    # API endpoints
    path('api/bookings/<str:date_str>/', views.api_bookings_by_date, name='api_bookings_by_date'),
    path('api/my-bookings/<str:phone>/', views.api_bookings_by_phone, name='api_bookings_by_phone'),
    path('api/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
