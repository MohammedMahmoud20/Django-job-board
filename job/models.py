from django.db import models

# Create your models here.
JOB_TYPE=(
    ('FULL TIME','FULL TIME'),
    ('PART TIME','PART TIME'), 
)


def image_upload(instance,filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

class job(models.Model):
    title=models.CharField(max_length=100)
    #location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    descriptions=models.TextField(max_length=1000)
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    image=models.ImageField(upload_to=image_upload)
    experience=models.IntegerField(default=1)
    Category= models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
       return self.title


class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
