from django.db import models


class Article(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
