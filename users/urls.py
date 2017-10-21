from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'login/$', login, name='login'),
    url(r'user/details/$', details, name='user-details'),
    url(r'user/register/$', register, name='register'),
    url(r'user/password/reset/$', recover_password, name='recover_password'),
    url(r'logout/$', logout, name='logout'),
]
