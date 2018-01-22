from tigereye.models.seat import SeatStatus
from .helper import FlaskTestCase
from flask import json
from tigereye.helper.code import Code

pid = 1
sid_list = [1, 2]
sid = ','.join([str(i) for i in sid_list])
price = 5000
orderno = 'test-%s-%s' % (pid, sid)
seats = '1-200-5000,2-200-5000'


class TestApiSeat(FlaskTestCase):
    def test_seat_lock(self):
        locked_seats_num = len(sid_list)
        rv = self.get_succ_json('/seat/lock/',
                                method='POST',
                                orderno=orderno,
                                pid=pid,
                                sid=sid,
                                price=price)
        self.assertEqual(rv['data']['locked_seats_num'], locked_seats_num)
        # 确定锁定成功 数据写入数据库
        rv = self.get_succ_json('/play/seats/', pid=pid)
        succ_count = 0
        for seat in rv['data']:
            if seat['orderno'] == orderno:
                self.assertEqual(seat['status'], SeatStatus.locked.value)
                succ_count += 1
        self.assertEqual(succ_count, locked_seats_num)
        # 确实重复锁定会失败
        rv = self.get_json('/seat/lock/',
                           method='POST',
                           orderno=orderno,
                           pid=pid,
                           sid=sid,
                           price=price)
        self.assertEqual(rv['rc'], Code.seat_lock_failed.value)

    # @Validator(pid=int, sid=multi_int, orderno=str)
    def test_seat_unlock(self):
        unlocked_seats_num = len(sid_list)
        self.test_seat_lock()
        rv = self.get_json('/seat/unlock/',
                           method='POST',
                           orderno=orderno,
                           pid=pid,
                           sid=sid)
        print('-' * 70)
        print(rv['data'], rv['rc'])
        self.assertEqual(rv['data']['unlocked_seats_num'], unlocked_seats_num)

    # # @Validator(seats=multi_comlex_int, orderno=str)
    # # @route('/buy/', methods=['POST'])
    # def test_seat_buy(self):
    #     buy_num = len(sid_list)
    #     rv = self.get_succ_json('/seat/buy/',
    #                             method='POST',
    #                             orderno=orderno,
    #                             seats=seats)
    #     self.assertEqual(rv['data']['bought_seats_num'], buy_num)
