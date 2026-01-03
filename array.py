import array as arr
array_num = arr.array('i',[1,2,3,4,5,3,79,3])
print('original array:' +str(array_num))
print('the number occurance of number 3 is :' + str(array_num.count(3)))
array_num.reverse()
print('The reverse order of the following array')
print(str(array_num))