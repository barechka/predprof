# Загрузка данных из файла books_rowling.csv
def load_books_data(file_name):
    books_data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            book_info = line.strip().split(',')
            books_data.append(book_info)
    return books_data


# Последовательный алгоритм поиска книги по названию
def search_book_by_title(books_data, title):
    found_books = []
    for book in books_data:
        if title.lower() in book[2].lower():
            found_books.append((book[0], book[2]))
    return found_books


# Основная программа для взаимодействия с пользователем
def main():
    books_data = load_books_data('books_rowling.csv')

    while True:
        search_title = input("Введите название книги (для завершения введите 'хватит'): ")

        if search_title.lower() == 'хватит':
            print("Программа завершена.")
            break

        found_books = search_book_by_title(books_data, search_title)

        if found_books:
            for book_id, book_title in found_books:
                print(f"ID: {book_id} - Название: {book_title}")
        else:
            print("Данной книги в этой библиотеке нет")


if __name__ == "__main__":
    main()