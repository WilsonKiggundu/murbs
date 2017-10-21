
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', ''),
    url(r'^', include('users.urls')),
    url(r'^', include('dashboard.urls')),
]
