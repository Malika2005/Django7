from django.shortcuts import render, redirect
from .models import Book, Reader, BookRent

def show_start_page(request):
    return render(request, "index.html")

def show_showbooks_page(request):
    if request.method == "GET":
        context = {"books": Book.objects.all()}
    return render(request, "showBooks.html", context)

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('showbooks')

def show_reader_page(request):
    if request.method == "GET":
        context = {"readers": Reader.objects.all()}

    return render(request, "showReader.html", context)

def delete_reader(request, reader_id):
    reader = Reader.objects.get(id=reader_id)
    reader.delete()
    return redirect('showreader')

def show_rent_page(request):
    if request.method == "GET":
        context = {"rents": BookRent.objects.all()}

    return render(request, "showRent.html", context)

def delete_rent(request, rent_id):
    rent = BookRent.objects.get(id=rent_id)
    rent.delete()
    return redirect('showrent')

def show_addbook(request):
    if request.method == "POST":
        title = request.POST.get("book_title")
        author_name = request.POST.get("book_author_name")
        author_surname = request.POST.get("book_author_surname")
        genre = request.POST.get("book_genre")
        publication_year = request.POST.get("publication_year")
        page_count = request.POST.get("page_count")
        description = request.POST.get("description")

        Book.objects.create(title=title,
                            author_name=author_name,
                            author_surname=author_surname,
                            genre=genre,
                            publication_year=publication_year,
                            page_count=page_count,
                            description=description)

    return render(request, "addBook.html")


def show_addreader_page(request):
    if request.method == "POST":
        name = request.POST.get("reader_name")
        surname = request.POST.get("reader_surname")
        age = request.POST.get("reader_age")
        address = request.POST.get("reader_address")

        Reader.objects.create(name=name,
                              surname=surname,
                              age=age,
                              address=address)

    return render(request, "addReader.html")


def show_addrent_page(request):
    if request.method == "POST":
        title = request.POST.get("book_title")
        reader = request.POST.get("reader_surname")
        rent_date = request.POST.get("rent_date")
        return_date = request.POST.get("return_date")

        BookRent.objects.create(book_title=title,
                                reader_surname=reader,
                                rent_date=rent_date,
                                return_date=return_date)

    return render(request, "addRent.html")


