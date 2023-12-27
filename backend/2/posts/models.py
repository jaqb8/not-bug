from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ["-date_posted"]

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.date_posted.strftime("%d %B %Y")
