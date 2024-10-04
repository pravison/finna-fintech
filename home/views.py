from django.shortcuts import render, redirect
from django.contrib import messages
from . models import CompanyInfor, ContactMessage, About, Service, Team, Testimonial

# Create your views here.
def index(request):
    infor = CompanyInfor.objects.all().order_by('id').first()
    about = About.objects.all().order_by('id').first()
    services = Service.objects.all()
    teams = Team.objects.all()
    testimonies = Testimonial.objects.all()
    context = {
        'infor': infor,
        'about' :about,
        'services': services,
        'teams': teams,
        'testimonies': testimonies
    }
    return render(request, 'index.html', context)

def contact_us(request):
    infor = CompanyInfor.objects.all().order_by('id').first()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'Thanks for reaching out, we will reply within 24 hours')
        return redirect('index')
    context = { 'infor': infor}
    return render(request, 'message.html', context )