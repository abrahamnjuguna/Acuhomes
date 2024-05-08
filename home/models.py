from django.db import models
from django.core.validators import FileExtensionValidator
from random import sample

# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('design', 'Design Phase'),
        ('construction', 'Under Construction'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='project_poster_images/', 
                               validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], 
                               blank=True, null=True)
    # Additional relevant fields
    location = models.CharField(max_length=100, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    architect = models.CharField(max_length=100, blank=True, null=True)
    contractor = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title
    

    def get_random_projects():
        # Get all project instances from the database
        all_projects = Project.objects.all()

        # Check if there are more than 5 projects
        if len(all_projects) > 5:
            # If there are more than 5 projects, sample 5 random projects
            random_projects = sample(list(all_projects), 5)
        else:
            # If there are 5 or fewer projects, return all projects
            random_projects = all_projects

        return random_projects

    


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    class Meta:
        verbose_name = 'Project Image'
        verbose_name_plural = 'Project Images'

    def __str__(self):
        return f'Image for {self.project.title}'
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class Expert(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_members/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(upload_to='service_banners/')
    # Additional fields for more information about the service
    icon = models.ImageField(upload_to='service_icons/', blank=True, null=True)

    def __str__(self):
        return self.title