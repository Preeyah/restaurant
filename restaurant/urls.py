from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('book/', views.book_table, name='book_table'),
    path('bookings/', views.view_bookings, name='view_bookings'),
]

