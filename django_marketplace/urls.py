from django.contrib import admin
from django.urls import path
from core.views import index

urlpatterns = [
    path('', index, name='index_page'),
    path('contact/', index, name='contact_page'),
    path('admin/', admin.site.urls),
]
