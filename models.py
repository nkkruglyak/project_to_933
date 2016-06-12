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
                    Column('chosen', Integer, default=0))

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
    def __init__(self, name, chosen):
        self.name = name
        self.chosen = chosen

    def update(self, data):
        """Обновляет запись в базе по словарю новых значений"""
        with make_session() as session:
            obj = session.query(Genre).filter_by(id=self.id).first()
            for key, value in data.items():
                setattr(obj, key, value)
            session.commit()

mapper(Genre, users_table)
metadata.create_all(engine)


if __name__== '__main__':
    x = Genre('Учебник',0)
    x.chosen = 1
    print x