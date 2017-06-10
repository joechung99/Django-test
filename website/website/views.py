from django.http import HttpResponse
from django.shortcuts import render
import datetime
def homepage_view(request):
    now = datetime.datetime.now()
    return render(request, 'homepage_view.htm', {'currentTime': now,'dept':'土木研究所碩士班','title':'0551287張為舜'})
def hello(request):
    return HttpResponse("Hello World")
def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.datetime.now()),
    })
def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now        
    return HttpResponse(html)
def hours_ahead(request, offset):
    try: 
        offset = int(offset)
    except ValueError: 
        raise Http404() 
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset) 
    html = "In %s hour(s), it will be %s." % (offset, dt) 
    return HttpResponse(html)