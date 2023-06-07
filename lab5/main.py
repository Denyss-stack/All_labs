from num2words import num2words
name = input("Enter your name: ")
number = int(input("Enter your number: "))
words = num2words(number)
print(f"Hello {name}, your number is {words}")