# Temel kitap sınıfı
class Book:
    def __init__(self, title, author, publication_year):
        # Kitabın temel bilgileri
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = False  # Kitap ödünç alındı mı?
        self.borrowed_by = None   # Kim ödünç aldı?

    def show_info(self):
        # Kitabın bilgilerini ekrana yazdırır
        status = "Available" if not self.is_borrowed else f"Borrowed by {self.borrowed_by}"
        print(f"{self.title} by {self.author} ({self.publication_year}) - {status}")

    def borrow(self, user_name):
        # Kitap ödünç alınmamışsa, kullanıcıya verir
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrowed_by = user_name
            return True
        return False

    def return_book(self):
        # Kitap iade edilir
        self.is_borrowed = False
        self.borrowed_by = None

    def to_dict(self):
        # Kitap bilgilerini JSON'a uygun sözlük formatına çevirir
        return {
            "type": "Book",
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
        }

# Roman sınıfı, Book sınıfından türetilir
class Novel(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre  # Roman türü (örneğin: polisiye)

    def to_dict(self):
        # Roman bilgilerini JSON'a uygun hale getirir
        data = super().to_dict()
        data["type"] = "Novel"
        data["genre"] = self.genre
        return data

# Dergi sınıfı, Book sınıfından türetilir
class Magazine(Book):
    def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue  # Dergi sayısı (örneğin: Mayıs 2025)

    def to_dict(self):
        # Dergi bilgilerini JSON'a uygun hale getirir
        data = super().to_dict()
        data["type"] = "Magazine"
        data["issue"] = self.issue
        return data