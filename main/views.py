from django.shortcuts import render
from .models import Items

# Create your views here.
def show_cards(request):
    all_card = Items.objects.all().values()
    response = {'cards': all_card}
    # print(all_card)
    
    return render(request, 'show_cards.html', response)