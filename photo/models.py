from django.db import models
from django.utils import timezone

class Photo(models.Model):
    # 图片创建时间
    created = models.DateTimeField(default=timezone.now)
    # 图片对象
    img = models.ImageField(upload_to='photo/%Y%m%d/', blank=True)
    # 图片标题
    cap = models.CharField(max_length=100)
    # 图片描述内容
    info = models.CharField(max_length=200)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.cap
