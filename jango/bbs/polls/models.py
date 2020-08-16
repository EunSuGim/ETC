from django.db import models


class Posts(models.Model) :
    posts_title = models.CharField(max_length=300)
    posts_writer = models.CharField(max_length=200)
    posts_date = models.DateTimeField('date published')
    posts_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.posts_title


class Answer(models.Model) :
    Answer_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    Answer_title = models.CharField(max_length=300)
    Answer_writer = models.CharField(max_length=200)
    Answer_date = models.DateTimeField('date published')
    Answer_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Answer_title
# Create your models here.
