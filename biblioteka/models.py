from django.db import models



class Book(models.Model):

    nazwa = models.CharField(max_length=60)
    opis = models.TextField()
    gatunek = models.CharField(max_length=30)
    cena = models.DecimalField(max_digits=400, decimal_places=2)
    rok_wydania = models.IntegerField(null=True, blank=True)
    autor = models.CharField(max_length=30)
    zdjecie = models.ImageField(null=True, blank=False, upload_to='zdjecia_ksiazek')
    przecena = models.BooleanField()


    def __str__(self):
        return self.nazwa_with_wydanie()

    def nazwa_with_wydanie(self):
        return str(self.nazwa) + " (" + str(self.rok_wydania) + ")" # użycie stringa w tej funkcji aby w adminie pokazywałą sie nazwa i data

class Author(models.Model):

    imie_nazwisko = models.CharField(max_length=60)
    urodzony = models.IntegerField(null=True, blank=True)
    data_smierci = models.IntegerField(null=True, blank=True)
    zdjecie_autora = models.ImageField(null=True, blank=False)
    informacje = models.TextField()


class TopTen(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.TextField()



