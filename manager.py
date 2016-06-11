# coding: utf-8
from models import Genre, make_session


class GenreManager(object):
    """Класс обрабатывает запросы к базе данных  с объектами Genre"""

    table = Genre

    @classmethod
    def find_one(cls, genre):
        """Возвращает первую запись с жанром -- genre.
        Если ее нет возврщает None"""
        with make_session() as session:
            result = session.query(cls.table).filter_by(name=genre.decode('utf-8')).first()
            if result:
                session.expunge(result)
        return result

    @classmethod
    def create_genre(cls, genre, choosen):
        """Создает в базе запись жанра -- genre, индификатор выбора -- choosen(0 или 1)"""
        with make_session() as session:
            record = cls.table(genre.decode('utf-8'), choosen)
            session.add(record)

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


if __name__ == '__main__':
    print(GenreManager.is_empty())
    GenreManager.create_genre(u"Детектив", 1)
    GenreManager.create_genre(u"Детские книги", 0)
    w = GenreManager.find_one(u"Детектив")
    print(GenreManager.is_empty())

