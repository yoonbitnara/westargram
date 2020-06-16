from django.db import models
from signup.models import Signup
from django.db import IntegrityError

class Comment(models.Model):
    #유저 아이디
    user_id = models.CharField(max_length=50)

    #댓글내용
    comment_data = models.CharField(max_length=300)

    #최초 댓글 단 시간
    comment_time = models.DateTimeField(auto_now_add=True)

    #댓글 수정 시간
    comment_update = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    account = models.ForeignKey(Signup, on_delete=models.CASCADE)


    class Meta:
        db_table = 'comment'




# Create your models here.
