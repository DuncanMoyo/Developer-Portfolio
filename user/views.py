from django.shortcuts import render
from user.models import Skill, Categories, Achievements  # UserProfile
from posts.models import Post, Author


def index(request):
    latest = Post.objects.order_by('-timestamp')[:3]
    listed_achievements = Achievements.objects.all()
    compilation = Author.objects.all()
    featured = Skill.objects.filter(featured=True)
    #categories = Categories.objects.all  # didn't realise that i actually do not need this line of code
    context = {
        'object_list': compilation,
        'featured': featured,
        #'categories': categories,
        'listed_achievements': listed_achievements,
        'latest': latest,

    }
    return render(request, 'index.html', context)
