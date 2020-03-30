from django.db import models

class courses(models.Model):
    course_name=models.CharField(max_length=250,default="Not Available")
    course_code=models.CharField(max_length=100)
    course_credit=models.CharField(max_length=100,default="Not Available")
    course_detail=models.CharField(max_length=5000,default="Not Available")
    def __str__(self):
        return self.course_code

class reviews(models.Model):
    course_name=models.ForeignKey(courses,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    comment=models.CharField(max_length=500)
    reviewer=models.CharField(default="Anonymous",max_length=100)


