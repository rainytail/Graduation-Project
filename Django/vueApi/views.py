# Create your views here.

import speech_recognition as sr
from translate import Translator

from vueApi.models import UserInfo, ListenSource, Friend
from vueApi.models import UserListenResource
from vueApi.models import UserShare, UserPost

SAVE_ROOT = '/tmp/pycharm_project_92/static/videos/'

def hello_world(request):  # request参数就是http请求的对象
    return JsonResponse({
        "content": "content",
        "name": "name",
    })


# 登录api
# 使用authenticate函数来实现用户的登录
def api_login(request):
    # 获取参数
    user_name = request.GET.get('username')
    pwd = request.GET.get('password')
    print(user_name, pwd)

    user = UserInfo.objects.filter(username=user_name, password=pwd)
    # 用户存在
    if user:
        return JsonResponse({
            "code": 200,
            "success": "true",
        })

    # return JsonResponse({
    #     "result": 'error',
    # })

    # 验证失败
    # else:
    #     return JsonResponse({
    #         "code": 403,
    #         "success": "false",
    #         'error_message': '用户不存在'
    #     })

def api_userinfo(request):
    # 获取参数
    username = request.GET.get("username")
    user = UserInfo.objects.get(username=username)
    if user is None:
        return JsonResponse({
            "result": "false"
        })
    # user = user
    return JsonResponse({
        "id": user.userId,
        "label": user.userlabel,
        'password': user.password,
        "age": user.userage,
        "urge": user.user_urge,
        "avatar": user.avatar,
    })


def api_getvideos(request):
    username = request.GET.get("username")
    user = UserListenResource.objects.filter(username=username).values()
    # 对queryset进行序列化
    videos = []
    for v in user:
        vi = {'resourceName': v['resourceName'],
              'has_use_count': v['has_use_count'],
              'resourceUrl': v['resourceUrl']}
        videos.append(vi)
    # print("videos: ", videos)
    return JsonResponse({
        "videos": videos
    })


def GetVideoText(request):
    # url = request.GET.get('videoUrl')

    audio_file = 'http://81.70.183.49:8000/static/videos/1.wav'


    # # 读取MP3文件
    # audio = AudioSegment.from_mp3("static/videos/2.mp3")
    #
    # # 将MP3文件保存为WAV格式
    # audio.export("static/videos/2.wav", format="wav")

    # 设置音频文件的位置
    audio_file = 'static/videos/2.wav'

    # 创建 SpeechRecognition 对象
    r = sr.Recognizer()

    # 读取音频文件
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    # 识别音频文件
    txt = (r.recognize_sphinx(audio, language="en-US"))
    # sentences = sent_tokenize(txt)
    return JsonResponse({
        'result': "success",
        'text': txt,
    })


def api_register(request):
    # print(request)
    username = request.GET.get('username')

    if len(UserInfo.objects.filter(username=username)) != 0:
        return JsonResponse({
            "result": "failed",
            "error_message": "用户已存在"
        })
    else:
        password = request.GET.get('password')
        userage = request.GET.get('userage')
        user_urge = request.GET.get('user_urge')
        avatar = request.GET.get('avatar')
        # print(avatar)
        new_user = UserInfo(
            username = username,
            password = password,
            userage = userage,
            user_urge = user_urge,
            avatar = avatar,
            userlabel="好好学习，天天向上",
        )
        new_user.save()
        return JsonResponse({
            "result": "success"
        })


def api_getForeignListen(request):
    all_videos = ListenSource.objects.all().values()
    # 对queryset进行序列化
    videos = []
    for v in all_videos:
        vi = {'resourceName': v['resourceName'],
              'resourceUrl': v['resourceUrl'],}
        videos.append(vi)
    # print("videos: ", videos)
    return JsonResponse({
        "videos": videos
    })


def api_translate(request):
    # to_lang为需要转化的文本目标
    to_lang = request.GET.get("to_lang")
    text = request.GET.get("text")
    to_lang = 'Chinese'
    translator = Translator(to_lang=to_lang)
    result = translator.translate(text)
    return JsonResponse({
        "result": "success",
        "to_lang_text": result
    })


import datetime


def api_dailyaudio(request):
    # 根据当天的时间来初始化种子，使得随机数在同一天保持不变
    all_audios = ListenSource.objects.all().values()
    lens = len(all_audios)

    # 获取当天日期
    today = datetime.date.today()
    # 使用当天日期作为种子
    random.seed(today)
    daily_number = random.randint(0, lens - 1)

    return JsonResponse({
        "result": "success",
        "audio": all_audios[daily_number]
    })


def api_getNeighborhood(request):
    # query_set = serializers.serialize("json", UserShare.objects.all())
    query_set = UserShare.objects.all().values()

    all_share = []

    for share in query_set:
        sh = {
            'userId': share['userId'],
            'username': share['username'],
            'userlabel': share['userlabel'],
            'userage': share['userage'],
            'user_urge': share['user_urge'],
            'avatar': share['avatar'],
            'title': share['title'],
            'resourceName': share['resourceName'],
            'resourceUrl': share['resourceUrl'],
            'content': share['content'],
        }
        all_share.append(sh)

    return JsonResponse({
        'result': "success",
        'all_share': all_share,
    })


def api_insert_a_post(request):
    userId = request.GET.get("userId")
    username = request.GET.get("username")
    title = request.GET.get("title")
    content = request.GET.get("content")
    url = request.GET.get('resourceUrl')
    resourceType = request.GET.get('resourceType')
    post = UserPost(
        userId=userId,
        username=username,
        title=title,
        content=content,
        resourceUrl=url,
        resourceType=resourceType
    )
    post.save()
    return JsonResponse({
        "result": "success",
    })


def api_get_notebook(request):
    username = request.GET.get('username')
    # username='123'
    query_set = UserPost.objects.filter(username=username).values()
    notebook = []
    for query in query_set:
        note = {
            'userId': query['userId'],
            'username': query['username'],
            'title': query['title'],
            'content': query['content'],
            'resourceType': query['resourceType'],
            'resourceUrl': query['resourceUrl'],
        }
        notebook.append(note)
    return JsonResponse({
        'result': 'success',
        'notebook': notebook,
    })

from .toText import connect

def api_video2text(request):
    # return JsonResponse({
    #     'result': "success"
    # })
    path = '/tmp/pycharm_project_92/static/videos/test.wav'
    # path = 'http://81.70.183.49:8000/static/videos/1.mp3'
    # path = os.getcwd() + '/../static/videos/' + '1.mp3'
    result = connect(path)
    # print(result)

    return JsonResponse({
        "result": "success",
        'text': result.json()
    })


from vueApi.models import PastPapers


def api_get_past_papers(request):
    suitable = request.GET.get('suitable')
    query_set = PastPapers.objects.filter(suitable=suitable).values()
    result = []
    for query in query_set:
        past_paper = {
            'suitable': query['suitable'],
            'resourceName': query['resourceName'],
            'resourceUrl': query['resourceUrl'],
        }
        result.append(past_paper)
    return JsonResponse({
        'result': "success",
        'past_papers': result,
    })



from django.http import FileResponse


def api_download_file(request, file_name):
    # 假设音频文件存储在某个目录下，根据文件名找到文件路径
    audio_path = './static/videos/' + file_name
    print(audio_path)

    # 打开文件并创建 FileResponse 对象
    audio_file = open(audio_path, 'rb')
    response = FileResponse(audio_file)

    # 设置响应头，告诉浏览器将文件作为附件下载
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response


def api_get_user(request):
    userId = request.GET.get('userId')
    user = UserInfo.objects.get(userId=userId)
    return JsonResponse({
        'result': "success",
        'user': {
            'userId': user.userId,
            'username': user.username,
            'userlabel': user.userlabel,
            'userage': user.userage,
            'user_urge': user.user_urge,
            'avatar': user.avatar,
        },
    })


from vueApi.models import CloudFiles


def api_get_cloudfiles(request):
    userId = request.GET.get('userId')
    dir = request.GET.get('dir')
    # print("dir: ", dir)
    query_set = CloudFiles.objects.filter(userId=userId, dir=dir).values()
    cloudfiles = []
    for query in query_set:
        couldfile = {
            'userId': query['userId'],
            'filename': query['filename'],
            'filesource': query['filesource'],
            'fileId': query['fileId'],
            'dir': query['dir'],
            'is_dir': query['is_dir'],
        }
        cloudfiles.append(couldfile)
    return JsonResponse({
        'result': "success",
        'cloudfiles': cloudfiles,
    })


import os
import random


def api_upload(request):
    # return JsonResponse({
    #     'result': "success"
    # })
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES.get('file')
        if file is None:
            # print("file is None.")
            return JsonResponse({
                'result': 'error',
                'message': 'file is None.',
            })
        userId = request.POST.get('userId')
        filename = request.POST.get('filename')
        filesource = request.POST.get('filesource')
        dir = request.POST.get('dir')
        is_dir = request.POST.get('is_dir')
        salt = ""
        for i in range(0, 5):
            salt += str(random.randint(0, 9))
        filesource = salt + filesource
        # print("now print types: ", type(file), type(userId), type(filename), type(filesource))
        save_path = SAVE_ROOT + userId + dir + filesource
        print("save_path: ", save_path)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        cloudfile = CloudFiles(userId=userId, filename=filename, filesource=filesource, dir=dir, is_dir=is_dir)
        cloudfile.save()
        return JsonResponse({'message': 'File uploaded successfully'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def api_delete_files(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # 确保解码为 utf-8
            fileIds = data.get('fileIds', [])
            # return JsonResponse({"result": fileIds})
            for fileid in fileIds:
                file = CloudFiles.objects.get(fileId=fileid)
                file_path = '/tmp/pycharm_project_92/static/videos/' + file.filesource
                if os.path.exists(file_path):
                    os.remove(file_path)
                file.delete()
            return JsonResponse({'result': 'success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error decoding JSON', 'details': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def api_create_folder(request):
    dir = request.GET.get('dir')
    folder_name = request.GET.get('folder_name')
    userId = request.GET.get('userId')

    # dir后面本来就加了/
    path = SAVE_ROOT + userId + dir + folder_name
    os.makedirs(path, exist_ok=True)

    file = CloudFiles(userId=userId, filename=folder_name, filesource=path, dir=dir, is_dir='true')
    file.save()

    return JsonResponse({
        'result': "success"
    })


def api_share_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # 从请求体中加载 JSON 数据
        # message = data.get('message')  # 访问 JSON 中的数据
        userId = data.get('userId'),
        username = data.get('username'),
        userlabel = data.get('userlabel'),
        userage = data.get('userage'),
        userUrge = data.get('user_urge'),
        avatar = data.get('avatar'),
        title = data.get('title'),
        resourceName = data.get('resourceName'),
        resourceUrl = data.get('resourceUrl'),
        content = data.get('content'),

        # print(userId, type(userId), userId[0])
        
        # print("type: ", type(userId), type(username),
        #       type(userlabel), type(userage),
        #       type(userUrge), type(avatar)
        #       )

        # print(userId[0], username[0], userlabel[0], userage[0], userUrge[0],
        #       avatar[0], title[0], resourceName[0], resourceUrl[0], content[0])

        share = UserShare(
            userId=userId[0],
            username=username[0],
            userlabel=userlabel[0],
            userage=userage[0],
            user_urge=userUrge[0],
            avatar=avatar[0],
            title=title[0],
            resourceName=resourceName[0],
            resourceUrl=resourceUrl[0],
            content=content[0],
        )
        share.save()
        return JsonResponse({
            'result': 'success'
        })
    else:
        return JsonResponse({
            'result': 'error'
        })


def api_get_share_posts(request):
    userId = request.GET.get('userId')
    query_set = UserShare.objects.filter(userId=userId).values()

    posts = []

    for share in query_set:
        sh = {
            'userId': share['userId'],
            'username': share['username'],
            'userlabel': share['userlabel'],
            'userage': share['userage'],
            'user_urge': share['user_urge'],
            'avatar': share['avatar'],
            'title': share['title'],
            'resourceName': share['resourceName'],
            'resourceUrl': share['resourceUrl'],
            'content': share['content'],
        }
        # print(sh)
        posts.append(sh)

    return JsonResponse({
        'result': "success",
        'posts': posts,
    })


import shutil


def api_delete_folder(request):
    dir = request.GET.get('dir')
    folder_name = request.GET.get('folder_name')
    userId = request.GET.get('userId')

    folder_path = SAVE_ROOT + userId + dir + folder_name

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        file = CloudFiles.objects.get(filesource=folder_path)
        file.delete()
        try:
            shutil.rmtree(folder_path)
            # print("删除文件夹成功")
            return JsonResponse({
                'result': 'success',
            })
        except Exception as e:
            print("删除文件报错", e)

    return JsonResponse({
        'result': 'error',
    })


def api_get_friends(request):
    userId = request.GET.get('userId')
    query_set = Friend.objects.filter(userId=userId).values()
    friends = []
    for query in query_set:
        friend = {
            'userId': query['userId'],
            'friendId': query['friendId'],
        }
        friends.append(friend)
    return JsonResponse({
        'result': 'success',
        'friends': friends,
    })


def api_get_friend_info(request):
    userId = request.GET.get('userId')
    # print("userId: ", userId)
    user = UserInfo.objects.get(userId=userId)
    return JsonResponse({
        'result': 'success',
        'friend': {
            'userId': user.userId,
            'username': user.username,
            'userlabel': user.userlabel,
            'userage': user.userage,
            'user_urge': user.user_urge,
            'avatar': user.avatar,
        },
    })


def api_is_friend(request):
    user1Id = request.GET.get('meId')
    user2Id = request.GET.get('youId')
    try:
        Friend.objects.get(userId=user1Id, friendId=user2Id)
        return JsonResponse({
            'result': 'success',
            'answer': 'false',
        })
    except Exception as e:
        return JsonResponse({
            'result': 'success',
            'answer': 'true',
        })


def api_change_relationship(request):
    user1Id = request.GET.get('meId')
    user2Id = request.GET.get('youId')

    try:
        ship = Friend.objects.get(userId=user1Id, friendId=user2Id)
        ship.delete()
    except Friend.DoesNotExist:
        friend = Friend(userId=user1Id, friendId=user2Id)
        friend.save()

    return JsonResponse({
        'result': 'success'
    })


def api_change_user(request):
    userId = request.GET.get('userId')
    username = request.GET.get('username')
    password = request.GET.get('password')
    userage = request.GET.get('userage')
    user_urge = request.GET.get('user_urge')
    avatar = request.GET.get('avatar')
    label = request.GET.get('userlabel')
    print("userAge: ", userage, "user_urge", user_urge)
    # print(avatar)
    user = UserInfo.objects.get(userId=userId)
    if username != '': user.username = username
    if password != '': user.password = password
    if userage != '': user.userage = userage
    if user_urge != '': user.user_urge = user_urge
    if avatar != '': user.avatar = avatar
    if label != '': user.userlabel = label
    user.save()
    return JsonResponse({
        "result": "success"
    })