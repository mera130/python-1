string = input("enter a string you want to reverse: ")

string2 = ("")
 
for i in string:
    string2 = i + string2
    
print("the original string: ", string)
print("how it is in reversed: ", string2)