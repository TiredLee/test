from .helper import FlaskTestCase
from flask import json
from tigereye.helper.code import Code


class TestApiCinema(FlaskTestCase):
    def test_cinema_all(self):
        self.get_succ_json('/cinema/all/')
        # response = self.app.get('/cinema/all/')
        # # 断言
        # self.assertEquals(response.status_code, 200)
        # data = json.loads(response.data)
        # print(data)
        # self.assertEquals(data['rc'], Code.succ.value)

    def test_cinema_halls(self):
        self.assert_get('/cinema/halls/', 400)
        data = self.get_succ_json('/cinema/halls/', cid=1)
        self.assertIsNotNone(data['data'])

    # 进行测试
    # python - m unittest tests/test_api_cinema.py
    # 测试tests包里的所有测试
    # python -m discover
