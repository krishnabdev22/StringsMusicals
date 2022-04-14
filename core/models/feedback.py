from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    feed = models.TextField(max_length=200)

    @staticmethod
    def get_all_feeds():
        return Feedback.objects.all()
