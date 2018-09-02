from django.contrib import admin
from django.urls import path
from list.views import home, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', home ),
    path('contact/', contact )
]
