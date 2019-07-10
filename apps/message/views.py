# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from .models import UserMessage
# Create your views here.


@csrf_protect
def getform(request):
    #message = None
    #all_messages = UserMessage.objects.filter(name='eggsy')
    #if all_messages:
     #   message = all_messages[0]
      #  all_messages.delete()

    if request.method == 'POST':
        name = request.POST.get('name', 'Name')
        message = request.POST.get('message', 'Message')
        address = request.POST.get('address','Adress')
        email = request.POST.get('email','Email')
        user_message = UserMessage()
        user_message.Name = name
        user_message.Message = message
        user_message.Adress = address
        user_message.Email = email
        user_message.object_id = '1'
        user_message.save()
    return render(request, 'message_form.html')
    #return render_to_response('message_form.html', context_instance=RequestContext(request))
    #context = {'foo': 'bar'}
    #return render(request, 'message_form.html', context,)
    #return render(request, 'message_form.html', {'form': message_form})
    #return render_to_response('message_form.html', context=csrf(request))