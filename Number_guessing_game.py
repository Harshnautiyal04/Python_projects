import random 

num = int(input("How much number you want enter here : "))

rndm = random.randint(1,num)

attempts = 0 


while True:

    guess  = int(input(f"Guess a number from 1 to {num} : "))  

    attempts+=1
    if guess == rndm:
        print("Correct!")
        break
    elif guess > rndm:
        print("Too high!")
    else:
        print("Too low!")

print(f"Number of attempts you take to guess a number is  {attempts}.")