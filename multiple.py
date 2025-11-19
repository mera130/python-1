try:
    num1,num2 = eval(input('enter two number(use comma): '))
    result = num1/num2
    print('result is', result)
except ZeroDivisionError:
    print('division by zero is error!')
except SyntaxError:
    print("comma is missing between the two numbers")
except:
    print('wrong input')
else:
    print('no exception')
finally:
    print('this will execute no matter what')