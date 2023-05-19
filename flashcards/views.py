import json
from functools import reduce
import re
from django.forms import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DeckForm, CardForm
from .models import Deck, Card


# Create your views here.
def index(request):
    deck = Deck.objects.all()
    return render(request, 'home.html',{"Deck":deck})
    
def add_deck(request):
    if request.method == "POST":
        form = DeckForm(request.POST, request.FILES)   
        if form.is_valid():
            new_deck = form.save()
            return redirect('home')
    else:
        form = DeckForm()
    return render(request, 'add_deck.html', {'form': form})

def add_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            new_card = form.save()            
            return redirect("home")
    else:
        form = CardForm()
    return render(request, 'add_card.html', {'form': form})

def deck_detail(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    return render(request, 'deck_detail.html', {'deck':deck})

def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            new_card = form.save()
            return redirect('home')
    else:
        form=CardForm(instance=card)
        return render(request, 'edit_card.html', {'form':form})

def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == "POST":
        form = DeckForm(request.POST, request.FILES, instance=deck)
        if form.is_valid():
            new_deck = form.save()
            return redirect('deck_detail', pk=deck.pk)        
    else:
        form=DeckForm(instance=deck)
        return render(request, 'edit_deck.html', {'form':form})

def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    deck.delete()
    return redirect('home')
       
def ajax_add_card(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        card = request.POST.get('front')
        data['front'] = card
        form = CardForm(request.POST)

        if form.is_valid():
            card = form.save()
            data['saved'] = True
            data['card'] = card

    else:
        data = {'response': 'not ok'}
    return JsonResponse(data)

def score(Deck,):
    pass

def success(Card):
    pass