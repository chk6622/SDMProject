from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.


def top(request):
#     return render_to_response('web_framework/top.html',locals(),context_instance=RequestContext(request))
    return render(request, 'web_framework/top.html')

def center(request):
#     return render_to_response('web_framework/center.html',locals(),context_instance=RequestContext(request))
    return render(request, 'web_framework/center.html')

def down(request):
#     return render_to_response('web_framework/down.html')
    return render(request, 'web_framework/down.html')

def left(request):
#     return render_to_response('web_framework/left.html',locals(),context_instance=RequestContext(request))
    return render(request, 'web_framework/left.html')

def middel(request):
#     return render_to_response('web_framework/middel.html',locals(),context_instance=RequestContext(request))
    return render(request, 'web_framework/middel.html')

def right(request):
#     return render_to_response('web_framework/right.html')
    return render(request, 'web_framework/right.html')

def welcome(request):
#     return render_to_response('welcome.html',locals(),context_instance=RequestContext(request))
    return render(request, 'welcome.html')

