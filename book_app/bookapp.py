import os
import time

# -------------------------------
# Helpers for Visual UI
# -------------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("\n" + "═" * 55)
    print("📚  BOOK MANAGEMENT SYSTEM  📚".center(55))
    print("═" * 55 + "\n")

def slow_print(text, delay=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()


# -------------------------------
# Book Class
# -------------------------------

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"📖 '{self.title}' — {self.author} ({self.year})"


# -------------------------------
# Book Manager
# -------------------------------

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        clear()
        banner()

        if not self.books:
            print("📌 სია ცარიალია.\n")
            return

        print("📚 --- წიგნების სია ---\n")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")
        print("\n" + "─" * 55)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# -------------------------------
# Input Validation
# -------------------------------

def validated_year_input(prompt):
    while True:
        year = input(prompt)
        if year.isdigit() and 0 < int(year) <= 2025:
            return int(year)
        else:
            print("❗ შეიყვანე სწორი წელი (რიცხვი).")


# -------------------------------
# Main UI Loop
# -------------------------------

def main():
    manager = BookManager()

    while True:
        clear()
        banner()

        print("🔸 1. ➕ ახალი წიგნის დამატება")
        print("🔸 2. 📚 ყველა წიგნის ნახვა")
        print("🔸 3. 🔍 წიგნის მოძებნა")
        print("🔸 4. 🚪 გასვლა")
        print("─" * 55)

        choice = input("👉 აირჩიე მოქმედება (1-4): ")

        # 1 — Add book
        if choice == "1":
            clear()
            banner()
            slow_print("📘 ახალი წიგნის დამატება...\n")

            title = input("📌 წიგნის სათაური: ").strip()
            author = input("✍️  ავტორი: ").strip()
            year = validated_year_input("📅 გამოცემის წელი: ")

            if not title or not author:
                print("\n❗ ველები ცარიელია!")
                time.sleep(1.5)
                continue

            manager.add_book(Book(title, author, year))
            print("\n✅ წიგნი წარმატებით დაემატა!")
            time.sleep(1.5)

        # 2 — Show books
        elif choice == "2":
            manager.show_books()
            input("\n👉 Enter დააბრუნებს მენიუში...")

        # 3 — Search book
        elif choice == "3":
            clear()
            banner()

            keyword = input("🔍 შეიყვანე სათაური: ")
            result = manager.search_book(keyword)

            print("\n" + "─" * 55)
            if result:
                print("🎉 ნაპოვნია!\n")
                print(result)
            else:
                print("❗ ასეთი წიგნი არ მოიძებნა.")

            print("─" * 55)
            input("\n👉 Enter მენიუში დაბრუნებისთვის...")

        # 4 — Exit
        elif choice == "4":
            clear()
            banner()
            slow_print("👋 პროგრამა დასრულდა. ნახვამდის!\n")
            break

        else:
            print("❗ არასწორი არჩევანი.")
            time.sleep(1.2)


# -------------------------------
# Start App
# -------------------------------

if __name__ == "__main__":
    main()
    