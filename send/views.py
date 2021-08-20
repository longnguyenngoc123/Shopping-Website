from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
@login_required
def index(request):
    toemail = request.POST.get('toemail')
    if request.method == 'POST':
        send_mail('Hello, from food restaurant', 'You have successfully subcribe to our website, please contact us at +84119283747 for more informations'
        ,'longnguyenngoc.org@gmail.com',[toemail],fail_silently=False)
        return HttpResponseRedirect('monan')
    return render(request, 'send/send.html')