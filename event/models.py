from django.db import models
from django.utils import timezone

class Event(models.Model):
    # 事件创建时间
    created = models.DateTimeField(default=timezone.now)
    # 事件类别 (美食，景点，影视)
    category = models.CharField(max_length=10)
    # 事件标签
    label = models.CharField(max_length=10)
    # 事件内容
    content = models.CharField(max_length=30)
    # 是否完成事件
    is_finished = models.BooleanField(default=False)
    # 事件打卡信息
    info = models.TextField()

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return self.content
