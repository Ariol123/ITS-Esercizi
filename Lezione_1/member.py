
from terza_lez import Book


class Member:
    def __init__(self,name, member_id):
        self._name = name
        self._member_id = member_id
        self,_borrow_book: list[Book]= []


    def borrow_book(self, book ):
        if book in self._borrow_book:
            self.borrow_book.append(book)

    def return_book(self, book):
        if book in self._borrow_book:
            self._borrow_book.remuve(book)

    def str (self):
        return f"Name= {self._name}; Member_id={self._member_id}"
    
    @classmethod
    def from_strng(cls, in_str)
        subs = in_str.split(',')
        return cls(subs[0],subs[1])
