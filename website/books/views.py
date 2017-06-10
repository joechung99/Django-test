from django.http import HttpResponse
from django.shortcuts import render
from .models import Book,Author,Publisher
def search_form(request):
    return render(request, 'search_form.htm')
def search(request):
    books = None
    if 'q' in request.GET:
        q = request.GET['q']
        message = "You are search %r" %(q)
        books = Book.objects.filter(title__icontains=q)
        allbook=[]
        allauthor=[]
        allpublisher=[]
        for i in books:
            allbook.append(i)
            allpublisher.append(i.publisher)
            allauthor.append(i.authors.all())
        return render(request, 'search_results.html', {'message':message,'books': allbook,'authors':allauthor,'publishers':allpublisher})
def printall(request):
    books=[]
    authors = []
    publishers = []
    for p in Book.objects.all():
        print(p)
        books.append("%s " % (p.title))
    for p in Author.objects.all():
        authors.append("%s %s" % (p.first_name,p.last_name))
    for p in Publisher.objects.all():
        publishers.append("%s " % (p.name))
    return render(request, 'printall.html', {'books': books,'authors':authors,'publishers':publishers})
# Create your views here.
