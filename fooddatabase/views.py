from django.shortcuts import render
from .models import Profile


# Create your views here.

def profile_input_view(request):
    if request.method == 'POST':
        Profile.objects.create(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'])
    # Profiles = profile.objects.all()
    return render(request, 'Profile_user_log_in.html')


def test_index_view(request):
    return render(request, 'index.html')
