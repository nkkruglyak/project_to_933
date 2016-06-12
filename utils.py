# coding: utf-8
from external_resources import BookResources
from manager import GenreManager


def download_and_put_in_base():
    """Записывает в базу запись о жанре, если такой еще нету"""
    genres = BookResources.parse()
    for genre in genres:
        if not GenreManager.find_one({'name': genre}):
            GenreManager.create_genre(genre, 0)


def mark_genres_as_chosen_by_id( list_id):
    """По списку id отмечает жанры в базе"""
    for number in list_id:
        rec = GenreManager.find_one({'id': number})
        rec.update({'chosen': 1})


def read_base():
    records = GenreManager.find()
    return records


def prepare_list_of_genres_for_template():
    """Возвращает словарь специального вида. в котором по ключу 'message' лежат все имена объектов из базы"""
    records = GenreManager.find()
    data = [{'name': x.id , 'value': x.chosen, 'message': x.name} for x in records]
    return data


if __name__ == '__main__':
    download_and_put_in_base()
    print prepare_list_of_genres_for_template()


