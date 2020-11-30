from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from django.utils.timezone import now

# Create your models here.

# Not required initially


class Userprofile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='images', default='default/user.png')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.user)

# Model for Physics subject Lecture and PDFs


class Posts(models.Model):
    '''
    We can upload from django user interface
    '''
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=15, null=True, blank=True)
    author = models.CharField(max_length=50, null=True, blank=True)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    lecture = models.FileField(default=None, blank=True, upload_to='video')
    # lecture_youtube = EmbedVideoField(default=None, blank=True)
    pdf = models.FileField(default=None, blank=True, upload_to='pdfs')
    time_stamp = models.DateTimeField(auto_now_add=True)


class Youtube(models.Model):
    '''
    Can embed You Tube videos
    '''
    lecture = EmbedVideoField(default=None, blank=True)

    pdf = models.FileField(default=None, blank=True, upload_to='pdfs')
    time_stamp = models.DateTimeField(auto_now_add=True)
