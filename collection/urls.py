from django.urls import path
from .views import show_cards

app_name='collection'

urlpatterns = [
    path('', show_cards, name='show_cards'),
]