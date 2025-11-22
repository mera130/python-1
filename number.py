import random
playing = True
number = str(random.randint(0,9))
print("i will generate a number and you will have to guess it")
print('game ends when you guess correctly')
while playing:
    guess = input('give me your best shot \n')
    if number ==guess:
        print("congrats! YOU WIN")
        print('the number was indeed', number)
        break
    else:
        print("it wasnt correct, sorry")
    
