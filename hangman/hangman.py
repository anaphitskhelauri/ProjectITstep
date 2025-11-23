import random

# წინასწარ განსაზღვრული სიტყვების სია
words = ["სკოლა", "სათამაშო", "პითონი", "სტუდენტი", "ტექნოლოგია"]

# შემთხვევითი სიტყვის არჩევა
word = random.choice(words).lower()

# ფარული სიტყვა ქვედა ტირეებით
hidden_word = ["_"] * len(word)

# მაქსიმალური მცდელობები
max_attempts = 6
attempts = 0

# უკვე გამოცნობილი ასოები
guessed_letters = []

print("---- Hangman თამაში ----")
print("გამოიცანით სიტყვა:")

# თამაში მიმდინარეობს, სანამ მცდელობები არ ამოიწურება
while attempts < max_attempts and "_" in hidden_word:
    print("\nსიტყვა: ", " ".join(hidden_word))
    print(f"დარჩენილი მცდელობა: {max_attempts - attempts}")
    guess = input("შეიყვანე ასო: ").lower()

    # შემოწმება: მომხმარებელმა ერთ ასოზე მეტი არ შეიყვანოს
    if len(guess) != 1:
        print("გთხოვ, შეიყვანე ერთი ასო!")
        continue

    # შემოწმება: ხომ არ ჰქონდა უკვე გამოცნობილი ასო
    if guess in guessed_letters:
        print("ეს ასო უკვე გამოცნობილი გაქვს!")
        continue

    guessed_letters.append(guess)

    # თუ ასო არსებობს სიტყვაში
    if guess in word:
        print("ეს ასო არის სიტყვაში.")
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
    else:
        print("ასო არ არის სიტყვაში!")
        attempts += 1

# შედეგი
if "_" not in hidden_word:
    print("\nგილოცავ! შენ გამოიცანი სიტყვა:", word)
else:
    print("\nმცდელობები ამოიწურა. სიტყვა იყო:", word)
