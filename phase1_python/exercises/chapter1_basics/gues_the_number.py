import random
guessNumber = random.randint(1, 100)
chance = 10
print("===============Guessing the number===============")
while chance != 0:
    userInput = int(input('enter a values between 1 and 100: '))
    if userInput > guessNumber:
        print('too high')
        chance -= 1

    elif userInput < guessNumber:
        print('too low')
        chance -= 1
    else:
        print('you find it')
        print("Chance left ", chance)
        print("Guess number is ", guessNumber)
        break


