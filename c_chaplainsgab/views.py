from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings

def become_volunteer(request):
    if request.method == 'POST':
        name = request.POST.get('volunteer-name')
        email = request.POST.get('volunteer-email')
        subject = request.POST.get('volunteer-subject')
        message = request.POST.get('volunteer-message')
        cv_file = request.FILES.get('inputGroupFile02')

        full_message = f"Nom : {name}\nEmail : {email}\nMotif : {subject}\n\nMessage :\n{message}"

        email_msg = EmailMessage(
            subject="Nouvelle demande de bénévolat",
            body=full_message,
            from_email=settings.EMAIL_HOST_USER,
            to=['cchaplains.ga@domaine.com'],  # Remplacez par l'adresse e-mail de destination
        )

        if cv_file:
            email_msg.attach(cv_file.name, cv_file.read(), cv_file.content_type)

        email_msg.send()
        messages.success(request, "Votre demande a bien été envoyée. Merci pour votre engagement !")
        return render(request, 'be_volonteer/be_volonteer.html')

    return render(request, 'be_volonteer/be_volonteer.html')


def home(request):
    return render(request, 'home.html')  

def about(request):
    return render(request, 'activy/activity.html')

def be_volunteer(request):
    return render(request, 'be_volonteer/be_volonteer.html')

def contact(request):
    return render(request, 'contact/contact.html')

def a_propos(request):
    return render(request, 'mot_col_maj/mot_col.html')


def donate(request):
    return render(request, 'do_donate/do_donate.html')