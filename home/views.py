from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def home(request):
    title = 'Home'
    projects = Project.get_random_projects()
    services = Service.objects.all()
    promo_video = PromoVideo.objects.first()
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Check if the email already exists in the database
            if not Subscriber.objects.filter(email=email).exists():
                # Create a new subscriber object
                subscriber = Subscriber(email=email)
                # Save the subscriber object to the database
                subscriber.save()
            # Redirect to a success page or reload the current page
            return redirect('home')
    context = {
        'title':title,
        'projects':projects,
        'services':services,
        'promo_video':promo_video
    }
    return render(request, 'home/index.html', context)


def about(request):
    title = 'About'
    experts = Expert.objects.all()
    services = Service.objects.all()
    context = {
        'title':title,
        'experts':experts,
        'services':services,
    }
    return render(request, 'home/about.html', context)


def services(request):
    title = "Services"
    services = Service.objects.all()
    context = {
        'title': title,
        'services':services,
    }
    return render(request, 'home/services.html', context)


def single_service(request,pk):
    title = "Single Service"
    service_obj = Service.objects.get(id=pk)
    all_services = Service.objects.all()
    context = {
        'title':title,
        'service_obj':service_obj,
        'all_services':all_services
    }
    
    return render(request, 'home/single_service.html', context)


def portfolio(request):
    title = 'Portfolio'
    projects = Project.objects.all()
    project_categoriess = ProjectCategory.objects.all()
    context = {
        'title':title,
        'projects':projects,
        'project_categoriess':project_categoriess,
    }
    return render(request, 'home/portfolio.html', context)

def contact(request):
    title = 'Contact'
    context = {
        'title':title,
    }
    return render(request, 'home/contact.html', context)


def project_details(request, pk):
    title = 'Project Details'
    project_obj = Project.objects.get(id=pk)
    project_images = ProjectImage.objects.filter(project=pk)
    context = {
        'title':title,
        'project_obj':project_obj,
        'project_images':project_images,
    }
    return render(request, 'home/project_details.html', context)