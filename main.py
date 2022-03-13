#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for i in range(nr_letters):
  password += letters[random.randint(0,51)]

for i in range(nr_symbols):
  password += symbols[random.randint(0,8)]

for i in range(nr_numbers):
  password += numbers[random.randint(0,9)]

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password1 = ""
hard_password2 = ""
hard_password3 = ""

for i in range(nr_letters):
  hard_password1 += str(letters[random.randint(0,51)])

for i in range(nr_symbols):
  hard_password2 += str(symbols[random.randint(0,8)])

for i in range(nr_numbers):
  hard_password3 += str(numbers[random.randint(0,9)])

new_password = hard_password1+hard_password2+hard_password3
real_password = random.sample(new_password,len(new_password))

print((''.join(real_password)))
