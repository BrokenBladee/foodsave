from django.shortcuts import render
from .models import Profile, Foodshelf


# Create your views here.

def profile_input_view(request):
    if request.method == 'POST':
        Profile.objects.create(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
    # Profiles = profile.objects.all()
    return render(request, 'profile_user_log_in.html')


def grocery_list_view(request):
    return render(request, 'grocerylist.html')


def add_food_view(request):
    if request.method == 'POST':
        Foodshelf.objects.create(food_name=request.POST['food_name'], expiry_date=request.POST['expiry_date'],
                                 liter_kilogram=request.POST['liter_kilogram'], count=request.POST['count'])
    return render(request, 'foodadd.html')
