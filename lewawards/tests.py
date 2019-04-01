from django.test import TestCase
from .models import Project,Profile, Grade

class ProjectTestClass(TestCase):
       def setUp(self):
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
          self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
          self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')


       def tearDown(self):
           Profile.objects.all().delete()
           Project.objects.all().delete()
           Grade.objects.all().delete()

       def test_save_project(self):
         self.project.save_project()
         projects = Project.objects.all()
         self.assertTrue(len(projects) > 0)   

       def test_delete_project(self):
           self.project.save_project()
           self.project.delete_project()
           projects = Project.objects.all()
           self.assertTrue(len(projects) == 0) 

       def test_update_description(self):
           self.project.save_project()
           caption='kiki'
           self.project.update_description(caption)
           self.assertTrue( self.project.description == caption) 

class ProfileTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
          self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
          self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')
        
       def tearDown(self):
          Profile.objects.all().delete()
          Project.objects.all().delete()
          Grade.objects.all().delete()
       
       def test_save_profile(self):
         self.profile.save_profile()
         profiles = Profile.objects.all()
         self.assertTrue(len(profiles) > 0) 

        
       def test_delete_profile(self):
           self.profile.save_profile()
           self.profile.delete_profile()
           profiles = Profile.objects.all()
           self.assertTrue(len(profiles) == 0)  

       def test_update_bio(self):
           self.profile.save_profile()
           bio='kiki'
           self.profile.update_bio(bio)
           self.assertTrue( self.profile.bio == bio) 


class GradeTestClass(TestCase):
       def setUp(self):
          
          self.profile=Profile(id=1,photo='Rwanda',bio='Kigali',first_name='hello',last_name='okay',phone_number=908787)
          self.project=Project(id=1,screenshot='@heroo',name='koko',description="koko koko koko okruuuuuu",overall_grade=2,url='halooooooo')
          self.grade=Grade(id=1,design=2,usability=2,content=2,project=self.project,total=0,avg=3,comment='olright')

       def tearDown(self):
          Profile.objects.all().delete()
          Project.objects.all().delete()
          Grade.objects.all().delete()
        
  
       def test_save_grade(self):
         self.profile.save_profile()
         self.project.save_project()
         self.grade.save_grade()
         grades = Grade.objects.all()
         self.assertTrue(len(grades) > 0) 

        
       def test_delete_grade(self):
           self.profile.save_profile()
           self.project.save_project()
           self.grade.save_grade()
           self.grade.delete_grade()
           grades = Grade.objects.all()
           self.assertTrue(len(grades) == 0)  

       def test_update_comment(self):
           self.profile.save_profile()
           self.project.save_project()
           self.grade.save_grade()
           comment='kiki'
           self.grade.update_comment(comment)
           self.assertTrue( self.grade.comment == comment) 



# Create your tests here.
