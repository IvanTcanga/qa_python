# Описание тестов
 
## Тесты и их описание
 
1. **test_initial_books_genre_empty**  
   При инициализации словарь `books_genre` пустой.
 
2. **test_initial_favorites_empty**  
   Список `favorites` при инициализации пустой.
 
3. **test_initial_genre_contains_available_genres**  
   При инициализации `genres` равно `['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']`.
 
4. **test_initial_genre_age_rating_contains_restrictions_genres**  
   При инициализации `genre_age_rating` равно `['Ужасы', 'Детективы']`.
 
5. **test_add_new_book_1_book_has_been_added**  
   При добавлении 1 книги, должна добавиться 1 книга.
 
6. **test_add_new_book_2_same_name_1_added**  
   При добавлении 2 одинаковых книг, добавляется 1.
 
7. **test_add_new_book_with_length_name_from_1_to_40_char**  
   `name` может быть от 1 до 40 символов.
 
8. **test_negative_add_new_book_with_invalid_length_name**  
   Длина имени вне диапазона от 1 до 40 символов не должна приниматься.
 
9. **test_set_book_genre_book_from_books_genre_genre_is_set**  
   Устанавливается жанр книги, если книга есть в `books_genre` и её жанр входит в список `genre`.
 
10. **test_negative_set_book_genre_book_not_in_books_genre_genre_is_not_set**  
    Жанр не устанавливается, если книги нет в `books_genre`.
 
11. **test_negative_set_book_genre_book_in_books_genre_genre_not_in_genre_is_not_set**  
    Жанр не устанавливается, если её жанр не входит в `genre`.
 
12. **test_get_book_genre_book_from_books_genre_of_book**  
    Проверка, что выводится жанр книги по её имени.
 
13. **test_get_books_with_specific_genre_genre_from_list_genre_get_genre**  
    Проверка, что выводит список книг с определённым жанром.
 
14. **test_negative_get_books_with_specific_genre_empty_books_genre_empty_list**  
    Если словарь с фильмами пустой, метод вернет `[]`.
 
15. **test_negative_get_books_with_specific_genre_is_not_from_the_list_empty_list**  
    Если жанр не в списке жанров, метод вернет `[]`.
 
16. **test_get_books_genre_got_a_dict_books_genre**  
    Проверка, что выводит текущий словарь `books_genre`.
 
17. **test_get_books_for_children_got_books_for_children**  
    Проверка, что возвращает книги, которые подходят детям.
 
18. **test_add_book_in_favorites_book_in_books_genre_added_in_favorites**  
    Проверка, что добавляет книгу в избранное и книга находится в словаре `books_genre`, повторно книга не добавляется.
 
19. **test_delete_book_in_favorites_book_in_books_genre_deleted_in_favorites**  
    Проверка, что удаляется книга из избранного, если она там есть.
 
20. **test_get_list_of_favorites_books_got_list_of_favorites**  
    Проверка, что получаем список избранных книг.
