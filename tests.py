import pytest
from main import BooksCollector

@pytest.fixture(scope="function", autouse=True)
def collector():
    return BooksCollector()

@pytest.fixture(scope="session", autouse=False)
def book_names():
    return ('Преследователь', 'Мы', 'На берегах Сены','Темные аллеи')

class TestBooksCollector:

    def test_add_new_book_add_four_books(self, collector, book_names):
        for name in book_names:
            collector.add_new_book(name)

        assert len(collector.get_books_genre()) == len(book_names)


    @pytest.mark.parametrize(
        'name, result',
        [
            ('', False),
            ('А', True),
            ('А' * 2, True),
            ('А' * 39, True),
            ('А' * 40, True),
            ('А' * 41, False)
        ]
    )
    def test_add_new_book_name_length(self, name, result, collector):
        collector.add_new_book(name)

        assert (name in collector.get_books_genre()) == result

    def test_add_new_book_has_no_genre(self, collector):
        name = 'Гордость и зомби'
        collector.add_new_book(name)

        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize(
        'genre',
        [
            'Фантастика',
            'Ужасы',
            'Детективы',
            'Мультфильмы',
            'Комедии'
        ]
    )
    def test_set_book_genre(self, genre, collector):
        name = 'Гарри Поттер'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'genre',
        [
            'Роман',
            ''
        ]
    )
        
    def test_set_book_genre_invalid_genre(self, genre, collector):
        name = 'Ромео и Джульетта'

        collector.add_new_book(name)

        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == ''
        
    def test_get_books_with_specific_genre(self, book_names, collector):

        for name in book_names:
            collector.add_new_book(name)


        collector.set_book_genre(book_names[0], 'Фантастика')
        collector.set_book_genre(book_names[1], 'Фантастика')
        collector.set_book_genre(book_names[2], 'Детективы')
        collector.set_book_genre(book_names[3], 'Роман')

        assert collector.get_books_with_specific_genre('Фантастика') == [book_names[0], book_names[1]]

    @pytest.mark.parametrize(
        'book1, book2, book3, book4, book5, book6',
        [
            ('Гарри Поттер', 'Шерлок Холмс', 'Дракула',
             'Шрек', 'Трое в лодке', 'Маленький принц')
        ]
    )
    def test_get_books_for_children(self, book1, book2, book3, book4, book5, book6, collector):
        
        for name in [book1, book2, book3, book4, book5, book6]:
            collector.add_new_book(name)

        collector.set_book_genre(book1, 'Фантастика')
        collector.set_book_genre(book2, 'Детективы')
        collector.set_book_genre(book3, 'Ужасы')
        collector.set_book_genre(book4, 'Мультфильмы')
        collector.set_book_genre(book5, 'Комедии')

        assert collector.get_books_for_children() == [book1, book4, book5]

    @pytest.mark.parametrize(
            'book1, book2, book3',
            [
                ('Любовь и память', 'Записки из мертвого дома', 'Иуда Искариот')
            ]
        )
    def test_add_book_in_favorites(self, book1, book2, book3, collector):
        
        for name in [book1, book2, book3]:
            collector.add_new_book(name)

        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)
        collector.add_book_in_favorites(book3)

        assert collector.get_list_of_favorites_books() == [book1, book2, book3]


    def test_add_book_in_favorites_already_added(self, collector):
        collector.add_new_book('Иуда Искариот')

        collector.add_book_in_favorites('Иуда Искариот')
        collector.add_book_in_favorites('Иуда Искариот')

        assert collector.get_list_of_favorites_books() == ['Иуда Искариот']

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        
        collector.add_book_in_favorites('Осень патриарха')

        assert collector.get_list_of_favorites_books() == []

    
    def test_delete_book_from_favorites(self, book_names, collector):

        for name in book_names:
            collector.add_new_book(name)
        for name in book_names:
            collector.add_book_in_favorites(name)

        collector.delete_book_from_favorites(book_names[0])

        assert collector.get_list_of_favorites_books() == list(book_names)[1:]