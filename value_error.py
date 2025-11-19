try:
    number =  int(input('enter a number:'))
    print('the number entered', number)
except ValueError as ex:
    print('exception; ', ex)