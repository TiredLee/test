from tigereye.models import db, Model

"""
    id
    名称
    语言
    字幕
    上映日期
    版本（2D/3D/4D）
    模式（胶片/数字）
    屏幕尺寸
    简介
    状态
"""


class Movie(db.Model, Model):
    mid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    language = db.Column(db.String(32))
    subtitle = db.Column(db.String(32))
    show_date = db.Column(db.Date)
    vision = db.Column(db.String(16))
    model = db.Column(db.String(16))
    screen_size = db.Column(db.String(16))
    introduction = db.Column(db.Text)
    status = db.Column(db.Integer, index=True, nullable=False, default=0)

    @classmethod
    def create_test_data(cls, num=10):
        for i in range(1, num + 1):
            m = Movie()
            m.mid = i
            m.name = '电影名称 %s' % i
            m.subtitle = '中文'
            m.language = '英文'
            m.model = '数字'
            m.vision = '2D'
            m.screen_size = 'IMAX'
            m.introduction = '哈哈哈'
            m.status = 1
            db.session.add(m)
        db.session.commit()
        print('movie test data done!')
