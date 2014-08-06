from django.shortcuts import *
from django.http import HttpResponse,HttpResponseRedirect
from models import Upload,User
from django.template import RequestContext, loader
from forms import MessageForm,SignupForm

def home(request):
    str="my home page"
    return HttpResponse(str)

def index(request):
    return render(request,'hello.html')

def message(request):
    return render(request, 'messages.html', {})

def signup(request):
    if request.method == 'GET':        
        form = SignupForm()
        
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            user_entry = form.save()
    return render(request,'profile.html')
##            signup_entry = form.save()
##              return render(request,'profile.html', {'success':True})
    
##def profile(request):
##    form = ProfileForm(request.POST)
##    if form.is_valid():
##        profile_entry = form.save()
##        return render(request,'profile.html',)
##
def savemessage(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        entry = form.save()
        return render(request, 'messages.html', {'success':True})
    
def files(request):
    file_list = Upload.objects.all()
    print file_list 
    #template = loader.get_template('prjctapp/files.html')

    #context = RequestContext(request, {'file_list': file_list,})
    #return HttpResponse(template.render(context))
    context={'file_list':file_list}
    return render(request,'prjctapp/files.html',context)

def userprofile(request):
    if request.method == 'GET':  
        form = SignupForm
        
    else:
        form = SignupForm(request.POST, request.FILES)
        pic = handle_uploaded_file(request.FILES['upload'])
        print pic
        if form.is_valid():
            
            form.save()
            
        
    return render(request,'profile.html',{'success':True})
    
            
