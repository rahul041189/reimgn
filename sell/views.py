from django.shortcuts import render
from django.views.decorators.gzip import gzip_page
# Create your views here.


@gzip_page
def sell(request):
    return render(request, 'sell/sell.html', {})
