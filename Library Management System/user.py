# Kullanıcı sınıfı
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.borrowed_books = []  # Kullanıcının ödünç aldığı kitaplar

    def borrow_book(self, book):
        # Kullanıcı kitap ödünç alır
        if book.borrow(self.name):
            self.borrowed_books.append(book.title)
            print(f"{book.title} başarıyla ödünç alındı.")
        else:
            print(f"{book.title} zaten ödünç alınmış.")

    def return_book(self, book):
        # Kullanıcı kitap iade eder
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            print(f"{book.title} başarıyla iade edildi.")
        else:
            print("Bu kitabı ödünç almadınız.")

    def list_borrowed_books(self):
        # Kullanıcının ödünç aldığı kitapları listeler
        if not self.borrowed_books:
            print("Hiç kitap ödünç alınmamış.")
        else:
            print("Ödünç alınan kitaplar:")
            for title in self.borrowed_books:
                print(f"- {title}")

    def to_dict(self):
        # Kullanıcı bilgilerini JSON'a uygun hale getirir
        return {
            "name": self.name,
            "password": self.password,
            "borrowed_books": self.borrowed_books
        }