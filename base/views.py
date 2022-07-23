import email
from multiprocessing.connection import Client
from turtle import setundobuffer, title
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail


from base.models import Member, Service,Project, Testimony,Client

def indexPage(request):
    clients = Client.objects.all()
    members = Member.objects.all()[0:3]
    services = Service.objects.all()
    testimonies = Testimony.objects.all()[0:1]
    testimoniess = Testimony.objects.all()[1:]
    projects = Project.objects.all()[62:]  

    context = {'members': members, 'testimonies': testimonies, 'testimoniess': testimoniess, 'clients': clients, 'services': services, 'projects': projects}
    return render(request, 'base/index.html', context,)

def aboutPage(request):

    members = Member.objects.all()[0:3]
    clients = Client.objects.all()
    testimonies = Testimony.objects.all()[0:1]
    testimoniess = Testimony.objects.all()[1:]

    context = {'members': members, 'testimonies': testimonies, 'testimoniess': testimoniess, 'clients': clients}
    
    return render(request, 'base/about.html', context)

def contactPage(request):
    if request.method == "POST":
        contact_name = request.POST.get('contact-name')
        contact_email = request.POST.get('contact-email')
        contact_message = request.POST.get('contact-message')

        context = {'contact_name': contact_name, 'contact_email': contact_email,'contact_message':contact_message }
        
        contact_message = '''
        {}

        Email: {}
        '''.format(context['contact_message'], context['contact_email'])

        send_mail(context['contact_name'], contact_message, '',['ondijotyrell@gmail.com'])

        return render(request, 'base/contact.html', context)
    else:
        return render(request, 'base/contact.html')

def galleryPage(request):
    return render(request, 'base/gallery.html')

def profilePage(request, pk):
    profile = Member.objects.get(id=pk)
    profiles = Member.objects.all()

    context = {'profiles': profiles, 'profile': profile}
    return render(request, 'base/member-profile.html', context)

def projectsPage(request):

    project_list = Project.objects.all().order_by('-id')
    p = Paginator(project_list, 10)
    page = request.GET.get('page')

    projects = p.get_page(page)
    nums = "a"*projects.paginator.num_pages  

    testimonies = Testimony.objects.all()[0:1]
    testimoniess = Testimony.objects.all()[1:]

    context = {'projects': projects, 'nums': nums, 'testimonies': testimonies, 'testimoniess': testimoniess }
    return render(request, 'base/page1.html', context)

def servicesPage(request):

    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'base/services.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)


    context = {'project': project}

    return render(request, 'base/single-project.html', context)

def servicePage(request, pk):
    service = Service.objects.get(id=pk)
    services = Service.objects.all()

    context = {'service':service, 'services':services }
    return render(request, 'base/single-service.html', context)

def teamPage(request):
    members = Member.objects.all()[0:7]
    associates = Member.objects.all()[7:10]

    context = {'members': members, 'associates':associates}
    return render(request, 'base/team.html', context)

def searchPage(request):

    if request.method == "POST":
        q = request.POST['q']
        projects = Project.objects.filter(description__contains=q)


        context = {'q': q, 'projects': projects}
        return render(request, 'base/search.html', context)
    
    else:
       context = {}
       return render(request, 'base/search.html', context) 

# Create your views here

