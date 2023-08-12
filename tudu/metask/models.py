from django.db import models

class Videos(models.Model):
    video_number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    video_file = models.FileField(upload_to='media/')

    # def __str__(self):
    #     return self.title