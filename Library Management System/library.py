import json
from book import Book, Novel, Magazine
from user import User

# Kütüphane sınıfı
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Kütüphanedeki tüm kitaplar
        self.users = []  # Kayıtlı kullanıcılar

    def add_book(self, book):
        # Yeni kitap ekler
        self.books.append(book)

    def add_user(self, user):
        # Yeni kullanıcı ekler
        self.users.append(user)

    def show_all_books(self):
        # Tüm kitapları listeler
        for book in self.books:
            book.show_info()

    def login(self, name, password):
        # Kullanıcı giriş işlemi
        for user in self.users:
            if user.name == name and user.password == password:
                return user
        return None

    def save(self, filename):
        # Tüm verileri JSON dosyasına kaydeder
        data = {
            "books": [book.to_dict() for book in self.books],
            "users": [user.to_dict() for user in self.users]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load(self, filename):
        # JSON dosyasından verileri yükler
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.books = []
                for b in data["books"]:
                    # Kitap türüne göre nesne oluşturur
                    if b["type"] == "Novel":
                        book = Novel(b["title"], b["author"], b["publication_year"], b["genre"])
                    elif b["type"] == "Magazine":
                        book = Magazine(b["title"], b["author"], b["publication_year"], b["issue"])
                    else:
                        book = Book(b["title"], b["author"], b["publication_year"])
                    book.is_borrowed = b["is_borrowed"]
                    book.borrowed_by = b["borrowed_by"]
                    self.books.append(book)

                self.users = []
                for u in data["users"]:
                    user = User(u["name"], u["password"])
                    user.borrowed_books = u["borrowed_books"]
                    self.users.append(user)
        except FileNotFoundError:
            # Dosya yoksa hata vermez, boş başlar
            pass