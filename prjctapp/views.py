from django.shortcuts import *
from django.http import HttpResponse
from models import Upload
from django.template import RequestContext, loader

def home(request):
    str="my home page"
    return HttpResponse(str)

def index(request):
    return render_to_response('hello.html')

def message(request):
    return render(request, 'messages.html', {})

def profile(request):
    return render_to_response('profile.html')

def savemessage(request):
    return HttpResponse(request)
    
def files(request):
    file_list = Upload.objects.all()
    print file_list 
    #template = loader.get_template('prjctapp/files.html')

    #context = RequestContext(request, {'file_list': file_list,})
    #return HttpResponse(template.render(context))
    context={'file_list':file_list}
    return render(request,'prjctapp/files.html',context)
    

# Create your views here.
