from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
