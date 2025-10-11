h = float(input("enter your height(cm): "))
w = float(input("enter your weight in kg:"))

BMI = w / (h/100)*2
print("your BMI is:", BMI)

if BMI < 18.5:
    print("you are underweight")
    
elif BMI < 24.9:
    print("you are healthy")
    
elif BMI < 29.9:
    print('you are overweight')

elif BMI < 34.9:
    print('you are severly overweight')
    
elif BMI < 39.9:
    print('you are obese ')
    
else:
    print('you are severly obese')