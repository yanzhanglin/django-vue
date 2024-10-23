from django.db import models

# Create your models here.
class Question(models.Model):
    # 创建模型Question，其中有字段question_text(问题描述)，发布时间(pub_data)
    quetion_text = models.CharField(max_length=200)
    pub_date = models.DateField("date published")

class Choice(models.Model):
    # 创建模型Choice，其中有字段 choice_text(选项描述)，votes(当前得票数)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

