from django.http import HttpResponse
def home(request):
    html = '<html><body>Welcome to django!</body></html>'
    return HttpResponse(html)