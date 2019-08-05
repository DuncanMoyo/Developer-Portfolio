from django.shortcuts import render
from user.models import UserProfile, Skill


def index(request):
    compilation = UserProfile.objects.all()
    featured = Skill.objects.filter(featured=True)
    context = {
        'object_list': compilation,
        'featured': featured
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html', {})