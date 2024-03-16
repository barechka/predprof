def assign_label(rating):
    """
    Assigns a label to a book based on its rating.

    Args:
    rating (float): The rating of the book.

    Returns:
    str: The label assigned to the book.
    """
    if rating < 5:
        return "не рекомендовать"
    elif 5 <= rating < 8:
        return "рекомендовать после"
    else:
        return "рекомендовать в первую очередь"


# Открываем файл с книгами
with open('books.csv', 'r') as file:
    # Читаем строки из файла
    lines = file.readlines()

    # Создаем новый список для хранения книг с ярлыками
    books_with_labels = []

    # Проходим по каждой строке книги
    for line in lines:
        # Разделяем строку по запятым
        book_info = line.split(',')

        # Извлекаем информацию о книге
        book_id = book_info[0]
        authors = book_info[1]
        original_title = book_info[2]
        publication_year = book_info[3]
        title = book_info[4]
        rating = float(book_info[5])

        # Определяем ярлык для книги
        label = assign_label(rating)

        # Добавляем ярлык к информации о книге
        book_info.append(label)

        # Преобразуем информацию о книге обратно в строку
        book_line = ','.join(str(info) for info in book_info)

        # Добавляем книгу с ярлыком в список
        books_with_labels.append(book_line)

# Записываем список книг с ярлыками в новый файл
with open('books_grade.csv', 'w') as new_file:
    for book in books_with_labels:
        new_file.write(book + '\n')