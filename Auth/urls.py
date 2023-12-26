from django.urls import path
from .views import registration
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm

form = RegistrationForm()

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), {'extra_context': {'form': form}}, name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]
