from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .forms import RegistrationForm
from .models import CustomUser

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password1']  # Note: Use 'password1' to get the first password field

            # Create a CustomUser instance and save it
            user = CustomUser(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
            )
            user.set_password(password)
            user.save()

            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    return render(request, 'auth/registration.html', {
        'form': form
    })
