class Library:
    #-------------------------------------------------------------------------------------------------------------#
    def __init__(self):
        
        self.file = open("books.txt", "a+")
        self.file.seek(0)
        self.rows = len(self.file.readlines())
    #-------------------------------------------------------------------------------------------------------------#
    def __del__(self):
        
        self.file.close()
    #-------------------------------------------------------------------------------------------------------------#
    def listBooks(self):
        
        self.file.seek(0)
        books = self.file.read().splitlines()
        i = 1
        if books:
            for book in books:
                try:
                    title, author, year, pages = book.split(',')
                    print(f"{i})📘 {title}, {author}, {year}, {pages}")
                except:
                    print(f"{i})📘 {book}")
                i += 1
        else:
            print("Gösterilebilecek kitap bulunamadı.")
    #-------------------------------------------------------------------------------------------------------------#
    def addBook(self):
        
        title = input("Kitabın Adı: ")
        author = input("Kitabın Yazarı: ")
        year = input("Yayınlanma Yılı: ")
        pages = input("Sayfa Sayısı: ")
        
        book_info = f"{title},{author},{year},{pages}\n"

        self.file.seek(0)
        
        if any(title in book for book in self.file.readlines()):
            print("❗ Bu kitap, kütüphanede zaten kayıtlı.")     
        else:
            self.file.write(book_info)
            print(f"✅ {title}, kütüphaneye başarıyla eklendi.")
            self.rows += 1
    #-------------------------------------------------------------------------------------------------------------#
    def removeBook(self):
        
        title = input("Silmek istediğiniz kitabın ismini giriniz: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        temp = 0
        for book in books:
            if title not in book:
                updated_books.append(book)
            else:
                temp += 1
                removed = True
        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print(f"✅ {title} kitabı kütüphaneden başarıyla kaldırıldı.")
            self.rows -= temp
        else:
            print(f"❗'{title}' adlı kitap bulunamadı.")
    #-------------------------------------------------------------------------------------------------------------#
            
lib = Library()

while True:
    print("----------------📋 MENÜ 📋----------------")
    print(f"1)📚 Kitapları Listele(Şu an {lib.rows} adet)")
    print("2)📝 Kitap Ekle")
    print("3)📝 Kitap Kaldır")
    print("q)❌ Çıkış")
    print("------------------------------------------")

    choice = input("İşlem Seçiniz (1/2/3/q): ")
    print("------------------------------------------\n")

    if choice == '1':
        print("------------📚 Kitap Listesi 📚------------")
        lib.listBooks()
        print("------------------------------------------\n")
    elif choice == '2':
        print("-------------📝 Kitap Ekle 📝-------------")
        lib.addBook()
        print("------------------------------------------\n")
    elif choice == '3':
        print("--------------📝 Kitap Çıkar 📝-------------")
        lib.removeBook()
        print("------------------------------------------\n")
    elif choice == 'q':
        print("------------------------------------------")
        print("Exiting...")
        print("------------------------------------------\n")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
