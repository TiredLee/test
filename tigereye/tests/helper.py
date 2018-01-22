from urllib.parse import urlencode
from flask import json
from unittest import TestCase
import tigereye
from tigereye.configs.test import Testconfig
from tigereye.helper.code import Code


# unittest 先找tests包 再找TestCase子类 实例化运行setUp方法 运行test_xxx方法
class FlaskTestCase(TestCase):
    def setUp(self):
        app = tigereye.create_app(Testconfig)
        app.logger.disabled = True
        self.app = app.test_client()
        with app.app_context():
            from tigereye.models import db
            from tigereye.models.cinema import Cinema
            from tigereye.models.hall import Hall
            from tigereye.models.movie import Movie
            from tigereye.models.play import Play
            from tigereye.models.order import Order
            from tigereye.models.seat import Seat, PlaySeat

            db.create_all()
            Cinema.create_test_data(cinema_num=1, hall_num=3, play_num=3)
            Movie.create_test_data()

    def assert_get(self, uri, assertcode=200, method="GET", **params):
        if method == 'POST':
            rv = self.app.post(uri, data=params)
        else:
            if params:
                rv = self.app.get('%s?%s' % (uri, urlencode(params)))
            else:
                rv = self.app.get(uri)
        self.assertEquals(rv.status_code, assertcode)
        return rv

    def get200(self, uri, method="GET", **params):
        return self.assert_get(uri, 200, method, **params)

    def get_json(self, uri, method="GET", **params):
        rv = self.get200(uri, method, **params)
        return json.loads(rv.data)

    def get_succ_json(self, uri, method="GET", **params):
        data = self.get_json(uri, method, **params)
        self.assertEquals(data['rc'], Code.succ.value)
        return data
