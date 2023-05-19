
from django.forms import ModelForm
from .models import Card, Deck


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'user', 'image',]
    
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['front', 'back', 'deck']

