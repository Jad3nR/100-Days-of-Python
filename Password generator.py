import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nlet=int(input("How many letters?\n"))
nnum=int(input("How many numbers?\n"))
nsym=int(input("How many symbols?\n"))

password = []

for let in range(1, nlet+1):
    let_rand=random.choice(letters)
    password.append(let_rand)
for num in range(1, nnum+1):
    num_rand=random.choice(numbers)
    password.append(num_rand)
for sym in range(1, nsym+1):
    sym_rand=random.choice(symbols)
    password.append(sym_rand)

random.shuffle(password)

final_password = "".join(password)
print(f"Your password is {final_password}")