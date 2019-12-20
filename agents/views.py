from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .models import agents
from django.core.mail import send_mail
from django.views.decorators.gzip import gzip_page
# Create your views here.

@gzip_page
def agent_view(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        license_id = request.POST['license_id']
        password = request.POST['pass']
        type = request.POST['type']
        state = request.POST['state']
        country = request.POST['country']
        img = request.FILES['file']

        agent_model = agents(type=type, fname = fname, lname=lname,
                             agent_image=img, phone=number, state_license_id=license_id,
                             email=email, state = state, country=country,
                             password=password)
        agent_model.save()
        # email_subject = 'Query from '+ name
        # email_msg = msg + '\n From ... ' + email
        # from_email = 'soutshrama@gmail.com'
        # to_email = 'ravi@intellectainc.com'
        # send_mail(email_subject, email_msg, from_email, [to_email], fail_silently=False)
        context = {'submit_response' : 'Your Query submitted successfully. Our team will contact you within 24 Hrs.'}
        return render(request, 'contactus/contactus.html', context)
    else:
        return render(request, 'agents/agents.html', {})


