from django.shortcuts import render,redirect
from ecom import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string
import email.message
import smtplib

# Message
from django.contrib import messages

# Authnticate APIs
def contacts(request):
    if request.method == 'POST':
        mssge = request.POST['message']
        name = request.POST['name']
        email_user = request.POST['email']
        subject = request.POST['subject']

        data_content = {'msg':mssge,"yourname":name,'user_email':email_user,'subject':subject}
        email_content = render_to_string('contact/mail.html',data_content)

        mess = email.message.Message()
        mess['Subject'] = 'Welcome to E-Shop'
        mess['From'] = settings.EMAIL_HOST_USER
        mess['To'] = 'shubhamupadhyay1014@gmail.com'
        password = settings.EMAIL_HOST_PASSWORD
        mess.add_header('Content-Type','text/html')
        mess.set_payload(email_content)
        s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        s.starttls()
        s.login(mess['From'],password)
        s.sendmail(mess['From'],[mess['To']],mess.as_string())
        messages.info(request,'Thankyou for contact us, we will reply you shortly')

        return redirect("http://127.0.0.1:8000/contact/contacts")
    return render(request,'contact/contact.html',{"BASE_URL":settings.BASE_URL})