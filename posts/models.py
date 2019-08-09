from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
from tinymce import HTMLField
from user.models import Skill, Job


User = get_user_model()


class PostView(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    skills = models.ManyToManyField(Skill)
    job_name = models.OneToOneField(Job, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    content = HTMLField('Content', null=True, blank=True)
    phone = models.CharField(max_length=15, default=+27640506930)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    featured = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    content = HTMLField('Content', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

















