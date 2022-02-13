n = 5
guesses = 4
print("Total guesses are 5. Use it carefully")
while(guesses >= 0):
    inp = int(input("Guess the integer number : "))
    
    if inp > n:
        print("Go low a bit")
        print("Number of guesses left : ",guesses)
        guesses = guesses - 1
        continue
    elif inp < n: 
        print("Go high a bit")
        print("Number of guesses left : ",guesses)
        guesses = guesses - 1 
    else:
        print("Tada! You guessed right!")
        break
if guesses < 0:
    print("Game Over!")
