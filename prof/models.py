from django.db import models
from django.urls import reverse
# Create your models here.
class departments(models.Model):
    dept_name=models.CharField(max_length=200)
    def __str__(self):
        return self.dept_name

class professors(models.Model):
    prof_department=models.ForeignKey(departments,on_delete=models.CASCADE)
    prof_name=models.CharField(max_length=250)
    prof_pic=models.CharField(max_length=5000)
    prof_position=models.CharField(max_length=100,default="Not available")
    prof_ra=models.CharField(max_length=1000,default="Not available")
    prof_mail=models.CharField(max_length=100,default="Not available")
    prof_phone=models.CharField(max_length=50,default="Not available")
    review_sum=models.IntegerField(default=0)
    review_no=models.IntegerField(default=0)
    def __str__(self):
        return self.prof_name

class reviews(models.Model):
    prof=models.ForeignKey(professors,on_delete=models.CASCADE)
    rating=models.IntegerField(default=0)
    comment=models.CharField(max_length=500)
    reviewer=models.CharField(default='None',max_length=100)
    report=models.IntegerField(default=0)
    like=models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)
    '''rating_ed=models.IntegerField(default=0)
    rating_poc=models.IntegerField(default=0)
    rating_cq=models.IntegerField(default=0)'''
