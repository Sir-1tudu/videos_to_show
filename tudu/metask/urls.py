from django.urls import path
from .views import Font_view

urlpatterns = [
    path('', Font_view, name="index")
]
