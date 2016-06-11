# coding: utf-8
from contextlib import contextmanager

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()
users_table = Table('genre', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('choosen', Integer, default=0))

Session = sessionmaker(bind=engine)


@contextmanager
def make_session(Session=Session):
    """Контекстный мэнэджер создает соединение с базой.
     При выходе закрывает соединение. В случае ошибки откатывает изменения"""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Genre(object):
    """Обертка над информацией о жанре для сохранения в базу"""
    def __init__(self, name, choosen):
        self.name = name
        self.choosen = choosen

    def __repr__(self):
        return unicode(u"<Genre({}, {})>".format(self.name.decode('utf-8'), self.choosen))


mapper(Genre, users_table)
metadata.create_all(engine)
