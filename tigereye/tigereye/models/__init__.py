from flask_sqlalchemy import SQLAlchemy
from flask import json as _json
from datetime import datetime

db = SQLAlchemy()


class Model(object):
    def put(self):
        db.session.add(self)

    @classmethod
    def commit(cls):
        db.session.commit()

    @classmethod
    def rollback(cls):
        db.session.rollback()

    def save(self):
        try:
            self.put()
            self.commit()
        except Exception:
            self.rollback()
            raise

    @classmethod
    def get(cls, primary_key):
        return cls.query.get(primary_key)

    def delete(self):
        db.session.delete(self)

    def __json__(self):
        data = {}
        for k, v in vars(self).items():
            if k.startswith('_'):
                continue
                # self.key
            if isinstance(v, datetime):
                v = v.strftime('%Y-%m-%d %H:%M:%S')
            data[k] = v
        return data


class JSONEncoder(_json.JSONEncoder):
    def default(self, o):
        if isinstance(o, db.Model):
            return o.__json__()
        if type(o) == bytes:
            return o.decode('utf-8')
        return _json.JSONEncoder.default(self, o)
