from django.db import models

from django.db import models
from ckeditor.fields import RichTextField


class PersonalInformation(models.Model):
    name_complete = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    mini_about = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    cv = models.FileField(upload_to='cv', blank=True, null=True)

    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    mycv = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_complete


class About(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    description1 = models.TextField(blank=False, null=True)
    description2 = models.TextField(blank=False, null=True)
    about_avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.title



class Skills(models.Model):
    skill = models.CharField(max_length=50, blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    link =  models.URLField(blank=True, null=True)
    link1 = models.URLField(blank=True, null=True)
    link2 = models.URLField(blank=True, null=True)
    link3 = models.URLField(blank=True, null=True)
    link4 = models.URLField(blank=True, null=True)
    link5 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.skill
