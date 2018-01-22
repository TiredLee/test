from flask_classy import FlaskView
from tigereye.api import ApiView
from tigereye.helper.code import Code
from flask import jsonify, request
from tigereye.models.hall import Hall
from tigereye.models.seat import Seat
from tigereye.extensions.validator import Validator


class HallView(ApiView):
    @Validator(hid=int)
    def seats(self):
        hid = request.params['hid']
        hall = Hall.get(hid)
        if not hall:
            return Code.hall_does_not_exist, request.args
        hall.seats = Seat.query.filter_by(hid=hid).all()
        return hall