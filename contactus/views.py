from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import ContactUsInfo
from django.core.mail import send_mail
from django.views.decorators.gzip import gzip_page
# Create your views here.

@gzip_page
def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['massage']
        contactus_model = ContactUsInfo(name = name, email = email, msg = msg)
        contactus_model.save()
        email_subject = 'Query from '+ name
        email_msg = msg + '\n From ... ' + email
        from_email = 'soutshrama@gmail.com'
        to_email = 'ravi@intellectainc.com'
        send_mail(email_subject, email_msg, from_email, [to_email], fail_silently=False)
        context = {'submit_response' : 'Your Query submitted successfully. Our team will contact you within 24 Hrs.', 'blog': blog_display}
        return render(request, 'contactus/contactus.html', {})
    else:
        return render(request, 'contactus/contactus.html', {})


