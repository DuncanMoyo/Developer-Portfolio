from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=30)
    category_icon = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name


class Job(models.Model):
    job_title = models.CharField(max_length=20)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.job_title


class Skill(models.Model):
    skill_name = models.CharField(max_length=15)
    skill_level = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.skill_name


class Achievements(models.Model):
    achievement_icon = models.CharField(max_length=50)
    tally = models.IntegerField()
    description = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.description


class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    profile_picture = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    skills = models.ManyToManyField(Skill)
    job_name = models.OneToOneField(Job, on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.TextField()
    phone = models.CharField(max_length=15, default=+27640506930)

    def __str__(self):
        return self.name
