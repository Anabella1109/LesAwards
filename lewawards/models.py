from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    photo=models.ImageField(upload_to='images/',default='images/avatar.jpg')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    phone_number=models.IntegerField(null=True)
    country=models.CharField(max_length=100,default='unknown',null=True)
    

    def save_profile(self):
        self.save()
    def delete_profile(self):
       self.delete()

    def update_bio(self,bio):
         self.bio=bio
         self.save()
   

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Project(models.Model):
      name=models.CharField(max_length=100,null=True)
      screenshot=models.ImageField(upload_to='projects/',default='images/avatar.jpg')
      description=models.TextField(null=True)
      url=models.TextField(null=True)
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,unique=False)
      overall_grade=models.IntegerField(null=True)
      

      @classmethod
      def search_by_name(cls,search_term):
        projects = cls.objects.filter(name__icontains=search_term)
        return projects

      def save_project(self):
         self.save()

      def delete_project(self):
        self.delete()
       
      def update_description(self,cap):
         self.description=cap
         self.save()


class Grade(models.Model):
      design=models.IntegerField()
      usability=models.IntegerField()
      content=models.IntegerField()
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
      project=models.ForeignKey(Project)
      total=models.IntegerField()
      avg=models.IntegerField(null=True)
      comment=models.TextField(null=True)

      def save_grade(self):
         self.save()
      def delete_grade(self):
         self.delete()

      def update_comment(self,comment):
         self.comment=comment
         self.save()

