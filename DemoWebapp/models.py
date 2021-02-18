from django.db import models

# Create your models here.
#Here we define database related code database field and schema
#Each class we create here is subclass of django.db.models class

class allCourses(models.Model):
    courseName = models.CharField(max_length=200)
    instructorName = models.CharField(max_length=200)

class courseDetails(models.Model):
    course=models.ForeignKey(allCourses,on_delete=models.CASCADE)             #connecting courese to all courses when delete course it should be deleted from all courses that is why on_delete is used
    selfLearnigCouse = models.CharField(max_length=500)
    instructorBasedCourse = models.CharField(max_length=500)

#python manage.py makemigrations DemoWebapp This command will tell django that we made some changes to model and django should store this changes as a migration


#after running this command you will get id before __initial.py file which we will use to below command.
#sql migration takes migration names and return their sql
#python manage.py sqlmigrate DemoWebapp id (e.g:  0001__inital.py then command is python manage.py sqlmigrate DemoWebapp 0001)
#after sqlmigrate run python manage.py migrate command to apply  all changes i.e migration to database
