books = {
    1: {"title": "Война и мир", "autor": "Лев Толстой", "year": "1869"},
    2: {"title": "Дом в котором", "autor": "Мариам Петросян", "year": "2009"},
    3: {"title": "11/22/63", "autor": "Стивен Кинг", "year": "2011"},
    4: {"title": "451 градус по Фарингейту", "autor": "Рэй Брэдбери", "year": "1953"},
    5: {"title": "Зов Ктулху", "autor": "Говард Лавкрафт", "year": "1928"},
}
for bookid, bookinf in books.items():
    print(f"----------------------Книга{bookid}-----------------------")
    print(f"Название: {bookinf['title']}, Автор: {bookinf['autor']},")
    print(f"-------------------------{bookinf['year']}----------------------")
