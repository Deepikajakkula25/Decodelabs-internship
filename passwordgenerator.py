import random
import string
print("="*50)
print("RANDOM PASSWORD GENERATOR")
print("="*50)
while True:
    try:
        length=int(input("Enter password length(minimum 8):"))
        if length<8:
            print("password length should be atleast 8.")
            continue
        break
    except ValueError:
        print("Please enter a valid number")
uppercase=string.ascii_uppercase
lowercase=string.ascii_lowercase
numbers=string.digits
special="!@#$%^&*()_+"
password=[random.choice(uppercase),random.choice(lowercase),random.choice(numbers),random.choice(special)]
all_characters=uppercase+lowercase+numbers+special
for _ in range(length - 4):

    password.append(random.choice(all_characters))
random.shuffle(password)
final_password="".join(password)
if length >= 14:
    strength = "strong"
elif length >= 10:
    strength = "medium"
else:
    strength = "basic"
print("\ngenerated password:",final_password)
print("password strength:",strength)
print("\nThank you for using random password generator")        