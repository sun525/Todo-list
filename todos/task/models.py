from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # 内容
    text = models.CharField(max_length=150)
    # 是否完成
    completed = models.BooleanField(default=False)
    # 外键关联
    creator = models.ForeignKey(to=User)
