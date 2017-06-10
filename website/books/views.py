from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
	
def search_form(request):
    return render(request, 'search_form.htm')
def search(request):
    books = None
    if 'q' in request.GET:
        q = request.GET['q']
        try:
            message = "You are search %r" %(q)
            books = Book.objects.get(title=str(q))
            if(books):
                return render(request, 'search_results.html', {'message': message,'title': books.title,'publisher':books.publisher})

        except Exception as e:
            print('not found' + request.GET['q'])
    return render(request, 'search_results.html', {'message': message})

# Create your views here.
