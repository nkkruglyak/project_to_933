# coding: utf-8
from external_resources import BookResources
from manager import GenreManager


def download_and_put_in_base():
    """Записывает в базу запись о жанре, если такой еще нету"""
    genres = BookResources.parse()
    for genre in genres:
        if not GenreManager.find_one(genre):
            GenreManager.create_genre(genre,1)


def prepare_list_of_genres_for_template():
    """Возвращает словарь специального вида. в котором по ключу 'message' лежат все имена объектов из базы"""
    records = GenreManager.find()
    data = [{'name': 'name', 'value': 'value', 'message': x.name} for x in records]
    return data


if __name__ == '__main__':
    download_and_put_in_base()
    print(prepare_list_of_genres_for_template())


