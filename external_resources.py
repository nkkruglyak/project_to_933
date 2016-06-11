# coding=utf-8
import requests


class BookResources(object):
    """Логика для скачивание и извлечения данных"""
    html_address = 'http://fanread.ru/genre/'
    coding = None

    @classmethod
    def load(cls):
        """Скачивает код страницы cls.html_address.
        Возвращает текст в виде строки в кодировке Cp1251"""
        response = requests.get(cls.html_address)
        cls.coding = response.encoding
        return response.text.encode(cls.coding)

    @classmethod
    def filter_out_irrelevant_lines(cls):
        """Скачивает и фильтрует данные со страницы.
         Возвращает список строк с именами жанров"""
        lines = cls.load()
        begin_str = u'<div class="clr-menu"></div><h3>Жанры</h3>'.encode(cls.coding)
        end_str = u'</div></div>'.encode(cls.coding)
        begin_index = lines.index(begin_str)
        lines = lines[begin_index + 1:]
        end_index = lines.index(end_str)
        lines_needed = lines[:end_index]

        lines_with_genres = filter(lambda t: '/a' in t, lines_needed.split('\n'))
        return lines_with_genres

    @classmethod
    def parse(cls):
        """Парсит строки на поиск жанров.
        Возвращает оные."""
        lines = cls.filter_out_irrelevant_lines()
        lines_with_genre_at_end = map(lambda t: t.rsplit('</a></div>', 1)[0], lines)
        genres = map(lambda t: t.rsplit('>', 1)[1], lines_with_genre_at_end)
        decoded_genres = map(lambda d: d.decode('cp1251').encode('utf8'), genres)
        return decoded_genres


if __name__ == '__main__':
    print BookResources.parse()[0]
