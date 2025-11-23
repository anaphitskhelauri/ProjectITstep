# ფუნქცია თითოეული ოპერაციისთვის
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return "ნულზე გაყოფა დაუშვებელია!" 
    return a / b

print("---- კალკულატორი ----")

while True:  
    num1 = input("შეიყვანე პირველი რიცხვი: ")
    num2 = input("შეიყვანე მეორე რიცხვი: ")

    # ვამოწმებთ რიცხვები სწორია თუ არა
    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        print("გთხოვ სწორ რიცხვები შეიყვანო!")
        continue  # აბრუნებს ციკლის დასაწყისში

    num1 = float(num1)
    num2 = float(num2)

    # ოპერაციის არჩევა
    print("აირჩიე ოპერაცია: +  -  *  /")
    operation = input("ოპერაცია: ")

    # პირობითი ოპერატორები
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("არასწორი ოპერაცია!")
        continue

    print("შედეგი:", result)

    # ვეკითხებით გავაგრძელოთ თუ არა
    choice = input("გინდა გაგრძელება? (y/n): ")
    if choice.lower() != 'y':
        print("პროგრამა დასრულდა.")
        break
