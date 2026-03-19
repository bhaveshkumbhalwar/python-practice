import random

low= 1
high = 100

number = random.randint(low,high)

guesses=0
isRunning = True

print("-----------------guess the number game---------------------")
print(f"enter the number between {low} and {high}:")

while isRunning:
    
    guess = input("enter your guess: ")
    
    if guess.isdigit():
        guess= int(guess)
        guesses +=1
        
        if guess<low or guess>high:
            print("number is out of range")
            print(f" please enter the number between {low} and {high}:")
            
        elif guess<number:
            print("low! try again")
            
        elif guess>number:
            print("high! try again")
            
        else:
            print(f"you got it! the answer was {number}")
            print(f"the number of guesses you take : {guesses}")
            isRunning=False
            
    else:
        print("invalid guess")
        print(f" please enter the number between {low} and {high}:")
        
            