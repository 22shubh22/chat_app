from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Message

def home(request):
    print("XXXXXXXXXX__Debug__XXXXXXXXXXX")
    return HttpResponse("Babalu")

def read_chat(request):
    latest_message_list = Message.objects.order_by('-pub_date')
    context = {
        'latest_message_list': latest_message_list,
    }
    #output = '\n'.join([q.message_text for q in latest_message_list])
    #return HttpResponse(output)
    return render(request, 'chat/read_chat_page.html', context)