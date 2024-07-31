from django.contrib import admin
from django.urls import path
from core.views import index

# this is an unprofessional way to load images
# just to see how the project looks like
# don't use it in real project
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index_page'),
    path('contact/', index, name='contact_page'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
