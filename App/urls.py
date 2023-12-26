from django.urls import path
from .views import profile, index, upload_avatar, event_form, import_file_form, import_file, my_info, my_people, jury
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('event_form', event_form, name="event_form"),
    path('my_people/', my_people, name='my_people'),
    path('my_info/', my_info, name='my_info'),
    path('jury/', jury, name='jury'),
]

urlpatterns += [
    path('profile/', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]

urlpatterns +=[
    path('import_file_form/', import_file_form, name="import_file_form"),
    path('import_file/', import_file, name='import_file')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)