# coding: utf-8
from models import Genre, make_session


class GenreManager(object):
    """Класс обрабатывает запросы к базе данных  с объектами Genre"""

    table = Genre

    @classmethod
    def find_one(cls, query):
        """Возвращает первую запись с жанром -- genre.
        Если ее нет возврщает None"""
        if 'name' in query:
            query['name'] = query['name'].decode('utf-8')
        with make_session() as session:
            result = session.query(cls.table).filter_by(**query).first()
            if result:
                session.expunge(result)
        return result

    @classmethod
    def create_genre(cls, genre, chosen):
        """Создает в базе запись жанра -- genre, индификатор выбора -- choosen(0 или 1)"""
        with make_session() as session:
            #import ipdb; ipdb.set_trace()
            record = cls.table(genre.decode('utf-8'), chosen)  #
            session.add(record)
        return record

    @classmethod
    def find(cls):
        """Отдает все записи из базы. Если она пуста, возвращает None"""
        with make_session() as session:
            result = session.query(cls.table).all()
            for rec in result:
                session.expunge(rec)
        return result

    @classmethod
    def is_empty(cls):
        """Если в базе есть хоть одна запись возвращает True. Иначе False"""
        with make_session() as session:
            result = session.query(cls.table).count()
            return not bool(result)





