from django.shortcuts import render, get_object_or_404
from .models import Project, Profile, Skill, Experience


def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, "home.html", {
        "projects": projects,
        "profile": profile,
        "skills": skills,
        "experiences": experiences,
    })


def project_detail(request, slug: str):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "project_detail.html", {"project": project})


def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, "about.html", {
        "profile": profile,
        "skills": skills,
        "experiences": experiences,
    })

# Create your views here.
