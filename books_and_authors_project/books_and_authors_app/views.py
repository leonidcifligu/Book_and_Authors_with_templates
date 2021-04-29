from django.shortcuts import render, redirect
from books_and_authors_app.models import *

def book(request):
    context = {
        'books': Book.objects.all()
        
    }
    return render(request, 'book.html', context)

def add_book(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
    )
    return redirect('/')

def add_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes'],
    )
    return redirect('/authors')

def author(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'author.html', context)

def view_book(request,id):
    book = Book.objects.get(id=id)
    if request.method =='POST':
        author = Author.objects.get(id=request.POST['author'])
        book.authors.add(author)
        return redirect('/view_book/'+ id)

    context ={
      'book': book,
      'authors': Author.objects.all()
    }
    
    return render(request,'book_id.html',context)
    

def view_author(request,id):
    authors = Author.objects.get(id=id)
    if request.method =='POST':
        book = Book.objects.get(id=request.POST['book'])
        author.books.add(book)
        return redirect('/view_author/'+ id)
    context = {
        'authors' :author,
        'book' : Book.objects.all()
    }
    return render(request, 'author_id.html',context)

