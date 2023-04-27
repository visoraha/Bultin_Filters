from django.shortcuts import render
import datetime

# Create your views here.
def built_in_filters(request):
    dt=datetime.datetime.now()
    d={'data':'hai vinay how Are yoU WHAT ABOUT YOUR Studies','dt':dt,'c':22}
    return render(request,'built_in_filters.html',d)
