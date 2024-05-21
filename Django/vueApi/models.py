from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 用户信息
class UserInfo(models.Model):
    userId = models.AutoField(primary_key=True)
    # userId = models.CharField(max_length=22)
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    userlabel = models.CharField(max_length=1000)
    userage = models.CharField(max_length=100)
    user_urge = models.CharField(max_length=50)
    avatar = models.CharField(max_length=1000)


    def __str__(self):
        return self.username.__str__()

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


# 记录用户保存的音频
class UserListenResource(models.Model):
    userId = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    resourceName = models.CharField(max_length=32)
    has_use_count = models.IntegerField()
    # resourceUrl记录了用户资源的所在地
    resourceUrl = models.CharField(max_length=400)
    # models.B

    def __str__(self):
        return self.resourceName.__str__()

    class Meta:
        verbose_name = '用户保存音频'
        verbose_name_plural = '用户保存音频'


# 对自己的听力过程进行记录
class UserPost(models.Model):
    userId = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    resourceType = models.CharField(max_length=100)
    resourceUrl = models.CharField(max_length=200)

    def __str__(self):
        return self.username.__str__() + '  ' + self.title.__str__()

    class Meta:
        verbose_name = '用户听力记录'
        verbose_name_plural = '用户听力记录'


# 所有外刊听力
class ListenSource(models.Model):
    resourceName = models.CharField(max_length=200)
    resourceUrl = models.CharField(max_length=400)

    def __str__(self):
        return self.resourceName.__str__()

    class Meta:
        verbose_name = '外刊听力资源'
        verbose_name_plural = '外刊听力资源'


class UserVideos(models.Model):
    username = models.CharField(max_length=32)


# 社区用户动态
class UserShare(models.Model):

    # id = models.AutoField(primary_key=True)

    # userId = models.CharField(max_length=200)
    userId = models.CharField(max_length=22)
    username = models.CharField(max_length=1000)
    userlabel = models.CharField(max_length=1000)
    userage = models.CharField(max_length=100)
    user_urge = models.CharField(max_length=50)
    avatar = models.CharField(max_length=1000)
    # 分享
    shareId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    resourceName = models.CharField(max_length=200)
    resourceUrl = models.CharField(max_length=400)

    content = models.CharField(max_length=1000)

    class Meta:
        verbose_name = '社区动态'
        verbose_name_plural = '社区动态'

    def __str__(self):
        return self.username.__str__() + self.resourceName.__str__()


class PastPapers(models.Model):
    suitable = models.CharField(max_length=50)
    resourceName = models.CharField(max_length=200)
    resourceUrl = models.CharField(max_length=400)

    def __str__(self):
        return self.resourceName.__str__()

    class Meta:
        verbose_name = '真题听力'
        verbose_name_plural = '真题听力'


class CloudFiles(models.Model):
    userId = models.CharField(max_length=1000)
    fileId = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=2000)
    filesource = models.CharField(max_length=1000)
    dir = models.CharField(max_length=100, blank=True)
    is_dir = models.CharField(max_length=20)

    def __str__(self):
        return self.fileId.__str__() + self.userId.__str__() + "   " + self.filename.__str__()

    class Meta:
        verbose_name = '云盘资源'
        verbose_name_plural = '云盘资源'


class Friend(models.Model):
    userId = models.CharField(max_length=100)
    friendId = models.CharField(max_length=100)

    class Meta:
        verbose_name = '好友'
        verbose_name_plural = '好友'
