from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    adress = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Authors(models.Model):
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    news_paper_name = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name
class Articles(models.Model):
       title = models.TextField(max_length=222,null=True)
       author = models.ForeignKey(Authors,related_name='articles',on_delete=models.CASCADE,null=True)
       content = models.TextField(null=True)
       published_date = models.DateField(auto_now=True)
       def __str__(self):
           return self.title
class Comments(models.Model):
    article = models.ForeignKey(Articles,related_name='comment',on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Users,related_name='usr',on_delete=models.CASCADE,null=True)
    content = models.TextField(null=True)
    created_At = models.DateField(auto_now=True)
    def __str__(self):
        return self.title