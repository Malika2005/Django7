from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    page_count = models.IntegerField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title} - {self.author_surname} - {self.genre}"


class Reader(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"


class BookRent(models.Model):
    book_title = models.CharField(max_length=50)
    reader_surname = models.CharField(max_length=30)
    rent_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book_title} was rent to {self.reader_surname}: {self.rent_date} to {self.return_date}"

