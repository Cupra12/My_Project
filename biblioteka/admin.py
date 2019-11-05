from django.contrib import admin
from .models import Book, Author, TopTen
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ('nazwa','gatunek')    # filtrowanie to co chcemy pokazać userowi
    list_display = ('nazwa','gatunek','rok_wydania','autor')
    list_filter = ('rok_wydania','gatunek')
    search_fields = ('nazwa', 'opis')



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('imie_nazwisko','urodzony')




@admin.register(TopTen)
class TopTenAdmin(admin.ModelAdmin):
    list_display = ('nazwa','opis')





