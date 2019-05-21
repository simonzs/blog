from tornado.web import url
from api_gateway.handlers import (
    base,
    login
)

url_patterns = [
    (r'/', base.DemoHandler, {'handler':'base'}),
    (r'/(.+)/([a-z]+)', base.DemoHandler, {'handler':'base'}), #url 无名传参
    (r'/(?P<pattern1>.+)/(?P<pattern2>\d+)', base.DemoHandler, {'handler':'base'}), #url 有名传参
    (r'/api/v1/login', login.LoginHandler, {'handler':'login'}),
    url(r'/api/v1/logout', login.LogoutHandler, {'handler':'logout'}, name='logout'),
]
