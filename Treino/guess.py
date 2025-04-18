guess = 0
tries = 0

while guess != 6 and tries < 3:
    guess = int(input("Guess the number: "))
    tries += 1

if guess == 6:
    print("You got it!")
else:
    print("Out of tries. The number was 6.")
