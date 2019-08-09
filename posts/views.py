from django.shortcuts import render, get_object_or_404, reverse,redirect  # added these 3 for the link to the post shown in index
from .models import Post, Category, Author
from django.db.models import Q
from .forms import CommentForm, PostForm


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

        context = {
            'queryset': queryset
        }

        return render(request, 'search_results.html', context)


def blog(request, id):
    category_list = Category.objects.all()
    oldest = Post.objects.order_by('timestamp')[:3]
    blog_list = Post.objects.all()
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user.author  # added author as it was giving me this error (Cannot assign "<SimpleLazyObject: <User: admin>>": "Comment.user" must be a "Author" instance.)
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={'id': post.id}))

    context = {
        'blog_list': blog_list,
        'post': post,
        'form': form,
        'oldest': oldest,
        'category_list': category_list,

    }
    return render(request, 'blog.html', context)


def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'post_create.html', context)


def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': form.instance.id
            }))

    context = {
        'title': title,
        'form': form,
    }

    return render(request, 'post_update.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect(reverse('home'))
