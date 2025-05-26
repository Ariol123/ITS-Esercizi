from terza_lez import Book

if __name__ == '__main__':
    book_str: str = "La Divina Comedia, D Alighieri, 9999223344"
    divi_com = Book.from_string(book_str)
    print(divi_com)
