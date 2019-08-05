from django.shortcuts import render
from user.models import UserProfile, Skill, Categories


def index(request):
    compilation = UserProfile.objects.all()
    featured = Skill.objects.filter(featured=True)
    categories = Categories.objects.all
    context = {
        'object_list': compilation,
        'featured': featured,
        'categories': categories
    }
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html', {})