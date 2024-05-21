from django.apps import AppConfig

VERBOSE_APP_NAME = '数据库表单'

class VueapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vueApi'
    verbose_name = VERBOSE_APP_NAME
