class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            print("대출 완료")
            self.is_available = False
        else:
            print("이미 대출 중")

    def return_book(self):
        self.is_available = True
        print("반납완료")

    def info(self):
        print(f"{self.title}/{self.author}/{self.is_available}")
    
book = Book("파이썬 기초", "홍길동")
book.info()
book.borrow()
book.borrow()
book.return_book()
book.info()
