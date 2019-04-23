from django.conf.urls import include, url
from django.contrib import admin
from chat.views import hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello),
]