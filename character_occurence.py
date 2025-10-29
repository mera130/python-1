string = input("enter any word: ")
c = input("enter a character: ")

count = 0 
i = 0
while i < len(string):
    if string[i] == c:
        count = count+ 1
    i = i +1
    
print("the no. of times", c, "has appeared: ", count)