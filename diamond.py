n = int(input('enter the number of rows:'))
if n%2==0:
    half_diamond = int(n/2)
else:
    half_diamond = int(n/2)+1
space = half_diamond-1

for i in range(1,half_diamond+1):
    for j in range(1,space+1):
        print(end= " ")
    space -= 1
    num = 1
    for j in range(2*i -1):
        print(end=str(num))
        num += 1
    print()
    
space = 1 
for i in range(1,half_diamond):
    for j in range(1,space+1):
        print(end=' ')
    space += 1
    num = 1
    for j in range(1, 2*(half_diamond-i)):
        print(end=str(num))
        num += 1
    print()
   