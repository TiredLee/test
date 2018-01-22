from flask import current_app, request
from flask_classy import FlaskView


class MiscView(FlaskView):
    # 默认路由是类名/misc/ 配置成/
    route_base = '/'

    # index首页视图函数
    def index(self):
        return self.check()

    def check(self):
        current_app.logger.info('checked from %s' % request.remote_addr)
        return 'hello world'

    def error(self):
        1 / 0
