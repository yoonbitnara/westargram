from django.db import models


class Signup(models.Model):
    new_id = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    objects = models.Manager()

    class Meta:
        db_table = 'signup'
# Create your models here.
