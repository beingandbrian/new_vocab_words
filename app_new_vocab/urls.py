from django.urls import path
from app_new_vocab import views
from app_new_vocab.models import VocabWord, Creator

app_name = 'app_new_vocab'

urlpatterns = [
    #www.newenglishvocabulary.com/new-vocab/home
    path('home/', views.home, name='urlnamehome'),
    #www.newenglishvocabulary.com/new-vocab/about
    path('about/',views.about, name='urlnameabout'),
    #www.newenglishvocabulary.com/new-vocab/contact
    path('contact/', views.contact, name='urlnamecontact'),
    #www.newenglishvocabulary.com/new-vocab/words
    path('words/', views.list_words, name='urlnamewords'),
]
