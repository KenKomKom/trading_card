from django.urls import path
from .views import show_cards

app_name='main'

urlpatterns = [
    path('', show_cards, name='show_cards'),
]