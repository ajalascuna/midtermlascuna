from django.db import models

# Create your models here.

class Post(models.Model):
    #question_text = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    #pub_date = models.DateTimeField('date_published')
    date_created = models.DateTimeField('date_created')
    date_updated = models.DateTimeField('date_updated')
    content = models.CharField(max_length=200)


    def __str__(self):
        #return 'Question:{}'.format(str(self.question_text))
        return 'Title:{}'.format(str(self.title))

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    comment_text = models.CharField(max_length=200)
