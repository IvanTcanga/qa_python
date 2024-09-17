from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_initial_books_genre_empty(self):
        assert BooksCollector().books_genre == {}

    def test_initial_favorites_empty(self):
        assert BooksCollector().favorites == []

    def test_initial_genre_contains_available_genres(self):
        genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert BooksCollector().genre == genre

    def test_initial_genre_age_rating_contains_restrictions_genres(self):
        genre_age_rating = ['Ужасы', 'Детективы']
        assert BooksCollector().genre_age_rating == genre_age_rating

    def test_add_new_book_1_book_has_been_added(self):
        collector = BooksCollector()
        book_name = 'Чужой'
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre and len(collector.get_books_genre()) == 1

    def test_add_new_book_1_book_empty_value(self):
        collector = BooksCollector()
        book_name = 'Чужой'
        collector.add_new_book(book_name)
        assert collector.books_genre[book_name] == ''

    def test_add_new_book_2_same_name_1_added(self):
        collector = BooksCollector()
        book_name = 'Чужой'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'name',
        [
            'Ч',
            'Чу'
            'Чужой',
            'ЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужой',
            'ЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужо'
        ])
    def test_add_new_book_with_length_name_from_1_to_40_char(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'ЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧ',
            'ЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужойЧужой',
        ])
    def test_negative_add_new_book_with_invalid_length_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_book_from_books_genre_genre_is_set(self):
        name = 'Чужой'
        genre = 'Ужасы'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_negative_set_book_genre_book_not_in_books_genre_genre_is_not_set(self):
        name = 'Чужой'
        genre = 'Ужасы'
        collector = BooksCollector()
        collector.set_book_genre(name, genre)
        assert len(collector.books_genre) == 0

    def test_negative_set_book_genre_book_in_books_genre_genre_not_in_genre_is_not_set(self):
        name = 'Чужой'
        genre = 'Документальный'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    def test_get_book_genre_book_from_books_genre_of_book(self):
        name = 'Чужой'
        genre = 'Ужасы'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_genre_from_list_genre_get_genre(self):
        name = 'Чужой'
        genre = 'Ужасы'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_negative_get_books_with_specific_genre_empty_books_genre_empty_list(self):
        genre = 'Ужасы'
        collector = BooksCollector()
        assert collector.get_books_with_specific_genre(genre) == []

    def test_negative_get_books_with_specific_genre_is_not_from_the_list_empty_list(self):
        name = 'Чужой'
        genre = 'Исторический'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_got_a_dict_books_genre(self):
        name = 'Чужой'
        genre = 'Ужасы'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {name: genre}

    def test_get_books_for_children_got_books_for_children(self):
        children_film_name = 'Шрек'
        adult_film_name = 'Чужой'
        collector = BooksCollector()
        collector.add_new_book(children_film_name)
        collector.add_new_book(adult_film_name)
        collector.set_book_genre(children_film_name, 'Мультфильмы')
        collector.set_book_genre(adult_film_name, 'Ужасы')
        assert collector.get_books_for_children() == [children_film_name]

    def test_add_book_in_favorites_book_in_books_genre_added_in_favorites(self):
        name = 'Чужой'
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites and len(collector.favorites) == 1

    def test_delete_book_in_favorites_book_in_books_genre_deleted_in_favorites(self):
        collector = BooksCollector()
        name = 'Чужой'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    def test_get_list_of_favorites_books_got_list_of_favorites(self):
        collector = BooksCollector()
        name = 'Чужой'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]
