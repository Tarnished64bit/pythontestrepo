from book import Book

library = [
    Book("Перекресток воронов", "Анджей Сапковский"),
    Book("Дзен и искусство ухода за мотоциклом", "Роберт Персинг"),
    Book("Пикник на обочине", "Братья Стругацкие")
]

for book in library:
    print(f"{book.title} - {book.author}")