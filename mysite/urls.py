"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from flashcards import views


urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('flashcards/new',views.add_deck, name="add_deck"),
    path('flashcards/new/card', views.add_card, name="add_card"),
    path('flashcards/<int:pk>/', views.deck_detail, name="deck_detail"),
    path('flashcards/<int:pk>/editcard', views.edit_card, name="edit_card"),
    path('flashcards/<int:pk>/edit', views.edit_deck, name="edit_deck"),
    path('flashcards/<int:pk>/deckdelete', views.delete_deck, name="delete_deck"),
    path('api/cards/new', views.ajax_add_card, name="ajax_add_card"),
]
