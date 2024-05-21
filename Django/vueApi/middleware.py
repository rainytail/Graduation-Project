from django.contrib.sessions.models import Session
from django.utils.deprecation import MiddlewareMixin

class ForceSessionToExpireMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated:
            # 设置当前会话立即过期
            request.session.set_expiry(0)
        return response