from django.shortcuts import render
from .models import MenuItem
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.shortcuts import render, redirect
from .forms import BookingForm

@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'restaurant/book_table.html', {'form': form})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'restaurant/view_bookings.html', {'bookings': bookings})


@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'restaurant/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'restaurant/edit_profile.html', {'form': form})



def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('menu')
    else:
        form = UserCreationForm()
    return render(request, 'restaurant/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
    else:
        form = AuthenticationForm()
    return render(request, 'restaurant/login.html', {'form': form})
