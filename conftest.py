import pytest
from main import BooksCollector


@pytest.fixture(scope="function", autouse=True)
def collector():
    return BooksCollector()


@pytest.fixture(scope="session", autouse=False)
def book_names():
    return (
        'Преследователь',
        'Мы',
        'На берегах Сены',
        'Темные аллеи'
    )
