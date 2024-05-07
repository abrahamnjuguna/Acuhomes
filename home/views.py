from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def home(request):
    title = 'Home'
    projects = Project.get_random_projects()
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
        'projects':projects
    }
    return render(request, 'home/index.html', context)


def about(request):
    title = 'About'
    experts = Expert.objects.all()
    context = {
        'title':title,
        'experts':experts,
    }
    return render(request, 'home/about.html', context)


def services(request):
    return render(request, 'home/services.html')