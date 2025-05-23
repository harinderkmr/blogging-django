from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

now = datetime.now()
time = now.strftime("%d %B %Y")

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Post Model
class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    image = models.ImageField(upload_to='images/posts', blank=True, null=True)
    content = models.CharField(max_length=100000)
    time = models.CharField(default=time, max_length=100, blank=True)
    likes = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postname)

# Comment Model
class Comment(models.Model):
    content = models.CharField(max_length=200)
    time = models.CharField(default=time, max_length=100, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}.{self.content[:20]}..."

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000, blank=True)
