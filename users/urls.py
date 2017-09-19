from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'user/details/$', details, name='user-details'),
]
