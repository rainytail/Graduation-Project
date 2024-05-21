from django.contrib import admin
from .modelAdmin import UserShareAdmin, PastPapersAdmin, UserPostAdmin, FriendAdmin
from .modelAdmin import CloudFilesAdmin, ListenSourceAdmin, UserInfoAdmin, UserListenResourceAdmin
# Register your models here.

from vueApi import models

admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.UserListenResource, UserListenResourceAdmin)
admin.site.register(models.ListenSource, ListenSourceAdmin)
admin.site.register(models.UserPost, UserPostAdmin)
admin.site.register(models.PastPapers, PastPapersAdmin)
admin.site.register(models.UserShare, UserShareAdmin)
admin.site.register(models.CloudFiles, CloudFilesAdmin)
admin.site.register(models.Friend, FriendAdmin)


admin.site.site_header = 'En Player 后台管理'  # 设置header
admin.site.site_title = 'En Player 后台管理'          # 设置title