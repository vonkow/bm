from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	join_date = models.DateTimeField(default=datetime.now())
	about = models.TextField()
	website = models.CharField(max_length=255)
	def __unicode__(self):
		return self.user.username

class Project(models.Model):
	title = models.CharField(max_length=255)
	owner = models.ForeignKey(User)
	create_date = models.DateTimeField(default=datetime.now())
	description = models.TextField()
	def __unicode__(self):
		return self.owner.username+"'s "+self.title

class ProjectMod(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	def __unicode__(self):
		return self.project.title+" mod "+self.user.username

class ProjectCode(models.Model):
	project = models.ForeignKey(Project)
	version = models.CharField(max_length=255)
	date = models.DateTimeField(default=datetime.now())
	notes = models.TextField()
	code = models.TextField()
	def __unicode__(self):
		return self.project.title+" version "+self.version

class Prize(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	def __unicode__(self):
		return self.name

class ProjectPrize(models.Model):
	project = models.ForeignKey(Project)
	prize = models.ForeignKey(Prize)
	reward = models.TextField()
	def __unicode__(self):
		return self.project.title+" prize "+self.prize.name

class ProjectTestGorup(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	prize = models.ForeignKey(Prize)
	status = models.CharField(max_length=255) #THIS SHOULD BE ENUMish
	def __unicode__(self):
		return self.user.username+"'s tests for "+self.project.title

class ProjectTest(models.Model):
	group = models.ForeignKey(ProjectTestGroup)
	code = models.ForeignKey(ProjectCode)
	test_code = models.TextField()
	status = models.CharField(max_length=255) #THIS SHOULD BE ENUMish
	# this should be different
	def __unicode__(self):
		return self.group.user.username+"'s tests for "+self.group.project.title

class ProjectTestAttempt(models.Model):
	test = models.ForeignKey(ProjectTest)
	status = models.CharField(max_length=255) #THIS SHOULD BE ENUMish
	results = models.CharField(max_length=255) #Maybe not a charField
	browser = models.CharField(max_length=255) #Maybe not a charField
	os = models.CharField(max_length=255) #Maybe not a charField
	def __unicode__(self):
		return self.test.group.user.username+"'s tests for "+self.test.group.project.title
