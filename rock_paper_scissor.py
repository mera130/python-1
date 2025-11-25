import random
while True:
    user = input("enter a choice, rock/paper/scissor: ")
    action = ['rock', 'paper', 'scissor']
    computer_action = random.choice(action)
    print(f'\nyou chose {user}, computer chose {computer_action} \n')
    
    if user == computer_action:
      print(f'both payers entered{user}, its tie\n')
      
    elif user == 'rock':
        if computer_action == 'scissor':
            print('rock smashes scissor. you win!')
        else:
          print('paper covers rock. you loseee!')
          
    elif user == 'paper':
      if computer_action =='scissor':
        print('scissor cuts paper. you lose!')
      else:
        print('paper covers rock. you win!')
      
    elif user == 'scissor':
      if computer_action == 'paper':
        print('scissor cuts paper. you win!')
      else:
        print('rock smashes scissor. you lose!')
            
    play_again = input('y/n: ')
    if play_again != 'y':
      break
    
    
    