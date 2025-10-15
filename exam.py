medical_cause = input("did you have a medical cause? yes or no: ")
attend = int(input("enter the attendance : "))

if medical_cause == 'yes':
    print("you are allowed ")
else:
    if attend>=75:
        print("you are allowed")
    else:
        print("you are not allowed")