#Password generator Project
# nr_letters = random.randint(0,len(letters))
# nr_numbers = random.randint(0,len(numbers))
# nr_symbols = random.randint(0,len(symbols))

# #easy level
# password = ""
# for char in range(1,nr_letters+1):
#     password+=random.choice(letters)
#
# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
#
# for char in range(1,nr_numbers+1):
#     password+=random.choice(numbers)
#
# print(password)


import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8''9']
symbols = ['!','#','@','$','%','&','(',')','*','^']

print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#hard level
password_list = []
for char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))

for char in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")