from django.urls import path
from . views import homepage, count, about
urlpatterns = [
    path('', homepage, name='home'),
    path('count/', count, name='count'),
    path('about/', about, name='about'),
]
