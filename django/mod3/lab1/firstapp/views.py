from django.http import HttpResponse

# Create your views here.
def index(request):
    template = "<html>" \
                "This is your first view" \
                "</html>"
    
    return HttpResponse(content=template)

from datetime import date

def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
                "<html>".format(today)
    
    return HttpResponse(content=template)