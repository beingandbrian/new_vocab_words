from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from app_new_vocab.models import VocabWord, Creator
from django.views.generic import ListView
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "new_vocab/home.html")

def about(request):
    return render(request, "new_vocab/about.html")

def contact(request):
    return render(request, 'new_vocab/contact.html')

# def home(request):
#     #log_notes = LogNote.objects.all()
#     log_notes = LogNote.objects.order_by("-log_date")[:20]
#     print(log_notes)
#     context = {'note_list':log_notes}
#     print(context)
#     return render(request, "catalog/home.html",context)

#view to render all words
def list_words(request):
    words = VocabWord.objects.all()#connection to models.py
    context = {'words':words} #connection to html page providing the variables available in your html page
    return render(request, 'new_vocab/list_words.html', context)

