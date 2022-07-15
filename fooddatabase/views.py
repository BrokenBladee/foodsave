from django.shortcuts import render
from .models import Profile, Foodshelf


# Create your views here.

def profile_input_view(request):
    if request.method == 'POST':
        Profile.objects.create(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
    # Profiles = profile.objects.all()
    return render(request, 'profile_user_log_in.html')


def grocery_list_view(request):
    all_food_items = Foodshelf.objects.all()
    return render(request, 'grocerylist.html', {'all_food_items': all_food_items})


def add_food_view(request):
    return render(request, 'foodadd.html')
