from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('create_user', create_user, name = 'create_user'),
    path('view_users', view_users, name="view_users"),
    path('edit_user/<str:username>', edit_user, name='edit_user'),
    path('user/change_password', change_password, name="change_password")
]
