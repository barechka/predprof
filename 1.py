# Открываем файл с книгами и их рейтингами
with open('books_rowling.csv', 'r') as file:
    # Читаем строки из файла
    lines = file.readlines()
    # Создаем пустой список для хранения информации о книгах
    books = []
    # Пропускаем заголовок
    for line in lines[1:]:
        # Разделяем строку по запятым
        book_info = line.split(',')
        # Извлекаем информацию о книге
        original_title = book_info[2]
        authors = book_info[1]
        ratings_1 = float(book_info[3])
        # Добавляем информацию о книге в список
        books.append((original_title, authors, ratings_1))


    # Реализуем сортировку списка книг по рейтингу без использования встроенных функций сортировки
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0][2]
            less = [x for x in arr[1:] if x[2] <= pivot]
            greater = [x for x in arr[1:] if x[2] > pivot]
            return quicksort(less) + [arr[0]] + quicksort(greater)


    sorted_books = quicksort(books)

    # Выводим три книги с худшим рейтингом
    for book in sorted_books[:3]:
        print(f"{book[0]} - {book[1]} - {book[2]}")