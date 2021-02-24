from django.db import models



class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.school_name