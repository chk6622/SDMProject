from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse,JsonResponse
import json
from HappyManagement.models import TaskState
from Common import CommonTools
from django.utils import timezone
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

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def postpone(request):
    print 'execute postpone method!'
    mReturn={
                'text':'The system is out of order! Please communicate administrator!',
                'response_type':'ephemeral',
                "replace_original": True
            }
    parms = json.loads(request.POST.get('payload'))
    actions=parms.get('actions')
    if actions and len(actions)>0:
        task_id=actions[0].get('value')
        taskState=TaskState.objects.get(id=task_id)
        if taskState:
            notify_count=taskState.notify_count
            postponeTime=CommonTools.get_postpone_time(notify_count)
            nextNotifyTime=CommonTools.calcute_datetime(timezone.now(),postponeTime)
            notify_count+=1
            taskState.next_notify_time=nextNotifyTime
            taskState.notify_count=notify_count
            taskState.save()
            rMessage='Ok, I will notify you in %d minutes.' % postponeTime
            mReturn={
                'text':rMessage,
                'response_type':'ephemeral',
                "replace_original": True
            } 
    return JsonResponse(mReturn)














