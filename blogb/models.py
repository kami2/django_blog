from django.db import models
from django.utils import timezone
import datetime
from django.core.cache import cache
import os
from ckeditor.fields import RichTextField


class SingletonModel(models.Model):

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    class Meta:
        abstract = True

    def save (self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class TechNow(models.Model):
    tech_name = models.CharField(max_length=240)
    tech_description = models.CharField(max_length=300)
    tech_progress = models.IntegerField(default=0)
    tech_img = models.ImageField(upload_to='blogb/tech_img', default='Img 351x100px')
    tech_url = models.URLField(max_length=240, default="Url to doc site")

    def __str__(self):
        return self.tech_name


class BlogSet(SingletonModel):
    site_title = models.CharField(max_length=240)
    short_title = models.CharField(max_length=240)
    site_name = models.CharField(max_length=240, default=None)
    slogan = models.CharField(max_length=240)
    logo = models.ImageField(upload_to='blogb/logo')

    def __str__(self):
        return self.site_title


class Author(SingletonModel):
    author_firstname = models.CharField(max_length=240, default='Firstname')
    author_surname = models.CharField(max_length=240, default='Surname')
    about = RichTextField(blank=True, null=True)
    email = models.EmailField(max_length=254)
    avatar = models.ImageField(upload_to='blogb/avatar')

    def __str__(self):
        return self.author_firstname


class Category(models.Model):
    name = models.CharField(max_length=240)
    slug = models.SlugField(max_length=240)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=240)
    title_short = models.CharField(max_length=340, default= "Krótki opis dla fancy odnosnikow obrazkowych")
    author = models.ForeignKey('Author', default=1, on_delete=models.CASCADE)
    content_text = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    photo_text = models.ImageField(upload_to='blogb/img_text', default= "pic_01.jpg")
    category = models.ManyToManyField('Category', default=1)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)






