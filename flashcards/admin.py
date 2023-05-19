from django.contrib import admin
from .models import Deck, User, Card

# Register your models here.
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(User)