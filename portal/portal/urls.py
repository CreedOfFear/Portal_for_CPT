from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main_page.urls', namespace='main_page')),
    path('admin/', admin.site.urls),
]
