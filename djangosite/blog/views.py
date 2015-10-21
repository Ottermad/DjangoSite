from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # create user
            pass
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})  
