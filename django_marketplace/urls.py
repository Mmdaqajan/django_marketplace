# this is an unprofessional way to load images
# just to see how the project looks like
# don't use it in real project
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from core.views import index, detail, signup, new, delete, edit, browse
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from core.forms import LoginFrom

urlpatterns = [
    path('', index, name='index_page'),
    path('browse/', browse, name='browse_page'),
    path('dashboard', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('contact/', index, name='contact_page'),
    path('signup/', signup, name='signup_page'),
    path('new-item/', new, name='new_item_page'),
    path('edit-item/<int:pk>', edit, name='edit_item_page'),
    path('delete-item/<int:pk>', delete, name='delete_item'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginFrom, template_name='core/login.html'), name='login_page'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>/', detail, name='detail_page'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

