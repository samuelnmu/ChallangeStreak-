# i = 5
# while i < 10:
#     print(i)
#     i = i+1
# print("Done")

# guessing game
secret_number = 7
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("Guess:  "))
    guess_count +=1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You Failed!")    