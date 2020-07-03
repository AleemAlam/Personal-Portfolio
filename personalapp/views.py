from django.shortcuts import render
from .models import AddServices,MyProject
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):

    services = AddServices.objects.all()
    projects = MyProject.objects.all()
    if request.method == 'POST':
        msg_name = request.POST['fname']+' '+request.POST['lname']
        msg_email = request.POST['email']
        msg_sub = request.POST['msgsub']
        msg_message ='message:\n'+request.POST['msg']
        msg_message+='\nName is:\n'+msg_name+'\nEmail is:\n'+msg_email

        send_mail(
        msg_sub,
        msg_message,
        settings.EMAIL_HOST_USER,
        ['aleem.alam@outlook.com'],
        )
        return render(request, 'index.html', {'services':services,'projects':projects,'name':msg_name})
    else:
        return render(request, 'index.html', {'services':services,'projects':projects})
