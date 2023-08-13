from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aspectapp/', include('aspectapp.urls')),
    path('comparisonapp/', include('comparisonapp.urls')),
]
