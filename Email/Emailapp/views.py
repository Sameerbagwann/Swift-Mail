from django.conf import settings
from django.shortcuts import render, redirect,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def sendmail(request):
    content={}
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        sender = settings.EMAIL_HOST_USER
        rec = request.POST['email']
        if subject and message and sender and rec:
            send_mail(subject, message,  sender,[rec],fail_silently=False)
            content['success']="Mail has been sent to  your gmail Successfully!!!"
            return render (request,"sendmail.html",content)
        else:
            content['Fail']='Invalid Credentials'
            return render(request,'sendmail.html',content)
    else:
        return render(request,'sendmail.html')