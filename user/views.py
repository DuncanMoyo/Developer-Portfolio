from django.shortcuts import render
from user.models import UserProfile, Skill, Categories, Achievements
from posts.models import Post


def index(request):
    latest = Post.objects.all()
    listed_achievements = Achievements.objects.all()
    compilation = UserProfile.objects.all()
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
