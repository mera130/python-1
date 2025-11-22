import random
while True:
    user = input("enter a choice, rock/paper/scissor: ")
    action = ['rock', 'paper', 'scissor']
    computer_action = random.choice(action)
    print(f'\nyou chose{user}, computer chose{computer_action} \n')
    
    if user == computer_action:
      print(f'both payers entered{user}, its tie\n')
    elif user == 'rock':
        if computer_action == 'paper':
            print('paper covers rock. you lose')
            
    
    
    