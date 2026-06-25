score = 0
print("Welcome to the General Knowledge Quiz!")
print("--------------------------------------")
answer = input("1.What is the capital of France?").strip().lower()
if answer == "paris":
    print("correct!")
    score += 1
else:
    print("Incorrect!The correct answer is paris.")
answer = input("\n2.which planet is known as red planet?").strip().lower()
if answer == "mars":
    print("correct!")
    score += 1
else:
    print("Incorrect! The correct answer is mars.")
answer = input("\n3.what is 5+7?").strip()
if answer == "12":
    print("correct!")
    score += 1
else:
    print("Incorrect!The correct answer is 12.")
print("\n-------------------------------------------")
print(f"Quiz completed!")
print(f"Your Final Score:{score}/3")
if score == 3:
    print("Excellent Performance!")
elif score == 2:
    print("Good Job!")
else:
    print("Keep Practicing!")                       