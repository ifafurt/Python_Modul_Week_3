# Gerekli sınıfları içe aktarıyoruz
from library import Library
from book import Novel, Magazine
from user import User

# Kütüphane nesnesi oluşturuluyor
lib = Library("My Library")

# Daha önce kaydedilmiş verileri JSON dosyasından yüklüyoruz
lib.load("library.json")

print("Kütüphane Sistemine Hoş Geldiniz")

# Kullanıcı giriş yapana kadar döngü devam eder
current_user = None
while not current_user:
    # Giriş veya hesap oluşturma seçeneği
    choice = input("1 - Giriş Yap\n2 - Hesap Oluştur\n> ")
    name = input("Kullanıcı Adı: ")
    password = input("Şifre: ")

    if choice == "1":
        # Kullanıcı giriş yapmaya çalışıyor
        current_user = lib.login(name, password)
        if not current_user:
            print("Bilgiler hatalı, tekrar deneyin.")
    elif choice == "2":
        # Yeni kullanıcı oluşturuluyor
        current_user = User(name, password)
        lib.add_user(current_user)
        print("Hesap oluşturuldu.")

# Giriş yaptıktan sonra ana menü döngüsü başlar
while True:
    print("Menü Seçenekleri:")
    print("1 - Tüm kitapları listele")
    print("2 - Kitap ödünç al")
    print("3 - Kitap iade et")
    print("4 - Ödünç aldığım kitapları göster")
    print("5 - Kaydet ve çık")

    option = input("> ")

    if option == "1":
        # Kütüphanedeki tüm kitaplar listelenir
        lib.show_all_books()

    elif option == "2":
        # Kullanıcı kitap ödünç almak istiyor
        title = input("Ödünç almak istediğiniz kitabın adı: ")
        for book in lib.books:
            if book.title == title:
                current_user.borrow_book(book)
                break
        else:
            print("Kitap bulunamadı.")

    elif option == "3":
        # Kullanıcı kitap iade etmek istiyor
        title = input("İade etmek istediğiniz kitabın adı: ")
        for book in lib.books:
            if book.title == title:
                current_user.return_book(book)
                break
        else:
            print("Kitap bulunamadı.")

    elif option == "4":
        # Kullanıcının ödünç aldığı kitaplar gösterilir
        current_user.list_borrowed_books()

    elif option == "5":
        # Veriler kaydedilir ve programdan çıkılır
        lib.save("library.json")
        print("Veriler kaydedildi. Görüşmek üzere!")
        break

    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.")