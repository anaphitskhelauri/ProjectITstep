import random

class GameBase:
    def start(self):
        raise NotImplementedError


class GuessNumberGame(GameBase):

    MAX_ATTEMPTS = 10  # მაქსიმალური მცდელობები

    def __init__(self, low, high):
        self.__low = low
        self.__high = high
        self.attempts = []  # მცდელობების მასივი

    def generate_number(self):
        return random.randint(self.__low, self.__high)

    def start(self):
        number = self.generate_number()

        print("\n🎮 Guess the Number თამაში 🎮")
        print(f"📌 გამოიცანი რიცხვი {self.__low}–{self.__high} შუალედში!")
        print(f"💡 გაქვს {self.MAX_ATTEMPTS} მცდელობა")
        print("✨ თამაში დაწყებულია...\n")

        while len(self.attempts) < self.MAX_ATTEMPTS:
            try:
                guess = int(input("👉 შეიყვანე რიცხვი: "))
            except ValueError:
                print("⚠️ შეიყვანე მხოლოდ მთელი რიცხვი!\n")
                continue

            self.attempts.append(guess)
            remaining = self.MAX_ATTEMPTS - len(self.attempts)

            if guess < number:
                print("🔼 უფრო მაღალია!\n")
            elif guess > number:
                print("🔽 უფრო დაბალია!\n")
            else:
                print("🎉 სწორია! გილოცავ!")
                print(f"📊 მცდელობების რაოდენობა: {len(self.attempts)}")
                return

            print(f"🕒 დარჩენილი მცდელობები: {remaining}\n")

        # თუ მოთამაშემ ყველა მცდელობა გამოიყენ
        print("💥 ყველა მცდელობა ამოიწურა — წააგე!")
        print(f"✔ სწორი რიცხვი იყო: {number}")


# =======================
#   მთავარი მენიუ
# =======================

def main_menu():
    while True:
        print("\n==============================")
        print("🎯 Guess The Number - მენიუ")
        print("==============================")
        print("1️⃣  თამაში")
        print("2️⃣  გასვლა\n")

        choice = input("👉 აირჩიე: ")

        if choice == "1":
            game = GuessNumberGame(1, 100)
            game.start()

        elif choice == "2":
            print("👋 ნახვამდის!")
            break

        else:
            print("❗ არასწორი არჩევანი!\n")


if __name__ == "__main__":
    main_menu()
