from django.db import models
#from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.core.urlresolvers import reverse

class Event(models.Model):
	created_date = models.DateTimeField(auto_now_add=True) 
	title = models.CharField(max_length=250, default="") 
	description = models.TextField(max_length=1500, default="")
	url = models.URLField(default="", blank=True, null=True)
	thumbnail = models.ImageField(blank=True, null=True)
	image = models.ImageField(blank=True,null=True)
	date = models.DateTimeField()
	slug = models.SlugField(max_length=300, blank=True)
	class Meta: 
		ordering = ['-date']

	def get_absolute_url(self):
		return reverse('event', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.title))
		super(Event, self).save(*args, **kwargs)

MODEL_TYPES = (
		('org', 'Organizer'),
		('lec', 'Lecturer')
	)

class Member(models.Model):
	created_date = models.DateTimeField(auto_now_add=True) 
	member_type = models.CharField(max_length=3, default='lec', choices=MODEL_TYPES)
	name = models.CharField(max_length=300, default='')
	description = models.CharField(max_length=300, default='Лектор', blank=True, null=True)
	email = models.EmailField(default='', blank=True, null=True)
	webpage = models.URLField(default='', blank=True, null=True)
	image = models.ImageField()
	slug = models.SlugField(max_length=300, blank=True)

	class Meta: 
		ordering = ['created_date']

	def get_absolute_url(self):
		return reverse('member', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name))
		super(Member, self).save(*args, **kwargs)

class Project(models.Model):
	created_date = models.DateTimeField(auto_now_add=True) 
	title = models.CharField(max_length=100, default="")
	description = models.CharField(max_length=500, default="", blank=True,null=True)
	github = models.CharField(max_length=100, default="https://github.com/")
	url = models.URLField(max_length=100, default="", blank=True, null=True)
	image = models.ImageField(null=True)
	slug = models.SlugField(max_length=100, blank=True)

	class Meta: 
		ordering = ['created_date']

	def get_absolute_url(self):
		return reverse('project', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.title))
		super(Project, self).save(*args, **kwargs)

class Partner(models.Model):
	created_date = models.DateTimeField(auto_now_add=True) 
	name = models.CharField(max_length=300, default="")
	description = models.CharField(max_length=300, default="", blank=True,null=True)
	url = models.URLField(max_length=100, default="", blank=True,null=True)
	image = models.ImageField()
	slug = models.SlugField(max_length=300, blank=True)

	class Meta: 
		ordering = ['created_date']
	
	def get_absolute_url(self):
		return reverse('partner', args=[str(self.slug)])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name))
		super(Partner, self).save(*args, **kwargs)

