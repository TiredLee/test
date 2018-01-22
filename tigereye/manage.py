from flask_script import Manager, Server, Shell
from tigereye.app import create_app
from tigereye.models import db
from tigereye.models.cinema import Cinema
from tigereye.models.hall import Hall
from tigereye.models.movie import Movie
from tigereye.models.play import Play
from tigereye.models.order import Order
from tigereye.models.seat import Seat, PlaySeat

app = create_app()
manager = Manager(app)


def _make_context():
    # locals() globals() 返回的是字典
    locals().update(globals())
    return dict(**locals())


manager.add_command('runserver', Server('127.0.0.1', port=5000))
manager.add_command('shell', Shell(make_context=_make_context))


@manager.command
def create_db():
    db.create_all()


@manager.command
def drop_db():
    db.drop_all()


@manager.command
def init_db():
    drop_db()
    create_db()


@manager.command
def test_data():
    from tigereye.models.cinema import Cinema
    from tigereye.models.movie import Movie
    Movie.create_test_data()
    Cinema.create_test_data()


if __name__ == '__main__':
    manager.run()
