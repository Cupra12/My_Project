from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import Page_Two
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm




# Create your views here.
def rejestarcja(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto utworzone dla {username}!') # wiadomość dla user i sukcesie zalłożenia konta
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'rejestracja.html', {'form': form})


def Moja_biblioteka(request):
    ksiazki = Book.objects.all() ### pokaż wszystkie ksiązki
    moze_ogladac = True
    return render(request, 'lista_ksiazek.html', {'ksiazki': ksiazki})

@login_required
def Nowa_ksiazka(request):
    form = Page_Two(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return  redirect(Moja_biblioteka)
    return render(request, 'Formularz_ksiazkowy.html', {'form': form})

@login_required
def Edytuj_ksiazke(request, id):
    ksiazki = get_object_or_404(Book, pk=id)
    form = Page_Two(request.POST or None, request.FILES or None, instance=ksiazki)

    if form.is_valid():
        form.save()
        return redirect('Ksiazki.html')
    return render(request, 'Formularz_ksiazkowy.html', {'form': form})

@login_required
def Usun_ksiazke(request, id):
    ksiazki = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        ksiazki.delete()
        return redirect(Moja_biblioteka)
    return render(request, 'Potwierdz_ksiazke.html', {'ksiazki': ksiazki})

@login_required
def Zbior_ksiazek(request):
    ksiazki = Book.objects.all()
    return render(request, 'Ksiazki.html', {'ksiazki': ksiazki})

@login_required
def Top_dziesiec(request):
    ksiazki = Book.objects.all()
    return render(request, 'top_ten.html',{'ksiazki': ksiazki})

@login_required
def Autorzy_ksiazek(request):
    ksiazki = Book.objects.all()
    return render(request, 'autorzy.html', {'ksiazki': ksiazki})




