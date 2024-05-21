from django.contrib.auth.views import LogoutView
from django.urls import path, include
import vueApi.views

urlpatterns = [
    # path('login', vue)
    path('hello_world/', vueApi.views.hello_world),
    path('login/', vueApi.views.api_login),
    path('getinfo/', vueApi.views.api_userinfo),
    path('getvideos/', vueApi.views.api_getvideos),
    path('gettext/', vueApi.views.GetVideoText),
    path('register/', vueApi.views.api_register),
    path('getforeignlisten/', vueApi.views.api_getForeignListen),
    path('translate/', vueApi.views.api_translate),
    path('dailyaudio/', vueApi.views.api_dailyaudio),
    path('getneighborhood/', vueApi.views.api_getNeighborhood),
    path('insert_a_post/', vueApi.views.api_insert_a_post),
    path('getNoteBook/', vueApi.views.api_get_notebook),
    path('video2text/', vueApi.views.api_video2text),
    path('getpastpapers/', vueApi.views.api_get_past_papers),
    path('download/<file_name>', vueApi.views.api_download_file),
    path('getUser/', vueApi.views.api_get_user),
    path('get_cloudfiles/', vueApi.views.api_get_cloudfiles),
    path('upload/', vueApi.views.api_upload),
    path('delete_files/', vueApi.views.api_delete_files),
    path('create_folder/', vueApi.views.api_create_folder),
    path('share_post/', vueApi.views.api_share_post),
    path('get_share_posts/', vueApi.views.api_get_share_posts),
    path('delete_folder/', vueApi.views.api_delete_folder),
    path('get_friends/', vueApi.views.api_get_friends),
    path('get_friend_info/', vueApi.views.api_get_friend_info),
    path('is_friend/', vueApi.views.api_is_friend),
    path('change_relationship/', vueApi.views.api_change_relationship),
    path('change_user/', vueApi.views.api_change_user),
    path('admin/logout/', LogoutView.as_view(), name='admin_logout'),
    
]