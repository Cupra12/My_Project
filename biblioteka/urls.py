from django.urls import path
from .views import Moja_biblioteka, Nowa_ksiazka, Edytuj_ksiazke, Usun_ksiazke, Zbior_ksiazek, Top_dziesiec, Autorzy_ksiazek
from . import views as user_views



urlpatterns = [
    path('Books/', Moja_biblioteka, name='Moja_biblioteka'),
    path('add/', Nowa_ksiazka, name='Nowa_ksiazka'),
    path('edit/<int:id>/', Edytuj_ksiazke, name='Edytuj_ksiazke'),
    path('delete/<int:id>/', Usun_ksiazke, name='Usun_ksiazke'),
    path('Ksiazki/', Zbior_ksiazek, name='Ksiazki'),
    path('top_ten/', Top_dziesiec, name='top_ten'),
    path('autorzy/', Autorzy_ksiazek, name='autorzy'),
    path('register/', user_views.rejestarcja, name='register'),



]

