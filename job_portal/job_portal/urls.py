from django.contrib import admin
from django.urls import path, include  # Include the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),  # Include the URLs from the profiles app
]

