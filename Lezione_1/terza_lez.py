

class Book:
    def __init__(self, title, author, isbn):
        self._title= title
        self._author=author
        self._isbn=isbn

    def str (self):
        return f"Title{self._title}; Author={self._author}; isbn = {self._isbn}"
    

    @classmethod
    def from_string(cls, repr_str: str):
        sub_strs = repr_str.split(',')
        return
