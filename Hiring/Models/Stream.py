from django.db import models

from Hiring.Models.School import School


class Stream(models.Model):
    stream_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School,on_delete=models.CASCADE)
    stream_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.stream_name