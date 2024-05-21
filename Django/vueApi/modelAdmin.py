from django.contrib import admin


class UserShareAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'resourceName', 'resourceUrl')
    search_fields = ('userId', 'username', 'resourceName')
    # list_display_links = ('userId', 'username', 'resourceName')

    class Media:
        css = {
            'all': ('../static/css/admin.css',)
        }


class PastPapersAdmin(admin.ModelAdmin):
    list_display = ('suitable', 'resourceName')
    search_fields = ('suitable', 'resourceName')
    # list_display_links = ('suitable', 'resourceName')


class CloudFilesAdmin(admin.ModelAdmin):
    list_display = ('fileId', 'userId', 'filename', 'filesource', 'is_dir')
    search_fields = ('fileId', 'userId', 'filename', 'filesource')
    # list_display_links = ('fileId', 'userId', 'filename', 'filesource', 'is_dir')


class ListenSourceAdmin(admin.ModelAdmin):
    list_display = ('resourceName',)
    search_fields = ('resourceName',)
    # list_display_links = ('resourceName', 'resourceUrl')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'password',
                    'userlabel', 'userage', 'user_urge', 'avatar')
    search_fields = ('userId', 'username', 'password',
                     'userlabel', 'userage', 'user_urge', 'avatar')
    # list_display_links = ('userId', 'username', 'password',
    #                       'userlabel', 'userage', 'user_urge', 'avatar')


class UserListenResourceAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'resourceName', 'has_use_count', 'resourceUrl')
    search_fields = ('userId', 'username', 'resourceName', 'has_use_count', 'resourceUrl')
    # list_display_links = ('userId', 'username', 'resourceName', 'has_use_count', 'resourceUrl')


class UserPostAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'title', 'content', 'resourceType', 'resourceUrl')
    search_fields = ('userId', 'username', 'title', 'content', 'resourceType', 'resourceUrl')
    # list_display_links = ('userId', 'username', 'title', 'content', 'resourceType', 'resourceUrl')


class FriendAdmin(admin.ModelAdmin):
    list_display = ('userId', 'friendId')
    search_fields = ('userId', 'friendId')
    # list_display_links = ('userId', 'friendId')