from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox_page'),
    path('new/<int:item_pk>', views.new_conversation, name='new'),
]
