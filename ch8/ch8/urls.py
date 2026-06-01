from django.contrib import admin
from django.urls import path
from app1.views import learn_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj/', learn_django, name='learn_django'),
    path('py/', learn_django, name='learn_django'),
]
