from django.db import models


# Post model
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    caption = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.caption[:]
