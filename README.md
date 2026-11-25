# Тестирование класса BooksCollector

В рамках учебного проекта написаны тесты на Python с использованием pytest.

## Список тестов

- `test_add_new_book_add_four_books` — проверка добавления четырёх книг.
- `test_add_new_book_name_length` — проверка длины названия книги.
- `test_add_new_book_has_no_genre` — проверка того, что новая книга не имеет жанра.
- `test_set_book_genre` — проверка присвоения допустимого жанра книге.
- `test_set_book_genre_invalid_genre` — проверка присвоения недопустимого жанра.
- `test_get_books_with_specific_genre` — проверка получения книг определённого жанра.
- `test_get_books_for_children` — проверка получения списка книг для детей.
- `test_add_book_in_favorites` — проверка добавления книг в избранное.
- `test_add_book_in_favorites_already_added` — проверка повторного добавления книги в избранное.
- `test_add_book_in_favorites_nonexistent_book` — проверка добавления несуществующей книги в избранное.
- `test_delete_book_from_favorites` — проверка удаления книги из избранного.
- `test_get_books_genre_returns_dictionary` — проверка получения словаря книг и их жанров.
- `test_get_book_genre_returns_correct_genre` — проверка получения жанра конкретной книги.
- `test_get_list_of_favorites_books_returns_list` — проверка получения списка избранных книг.

## Фикстуры

Фикстуры вынесены в отдельный модуль `conftest.py`.

- `collector` — создаёт новый объект класса BooksCollector для каждого теста.
- `book_names` — содержит названия книг, которые используются в нескольких тестах.

В некоторых тестах используется параметризация для проверки разных входных данных.

## Результаты

- Написано 14 тестовых функций.
- Все 24 тестовых случая успешно пройдены.
- Все 9 публичных методов класса BooksCollector имеют отдельные тесты.
- Покрытие строк кода — 100%.
