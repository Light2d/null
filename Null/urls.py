from django.contrib import admin
from django.urls import path,include

#Administrations
urlpatterns = [
    path('admin/', admin.site.urls),
]

#includes
urlpatterns += [
    path('',include('Admin.urls')),
    path('',include('Auth.urls')),
    path('',include('App.urls'))
]