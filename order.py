import numpy as np
data_type = [('name', 'S15') ,('class', int), ('height', float)]
student_detail = [('james', 5, 4.8 ), ('nil', 6, 52.6) ,('paul', 5, 68.2) ,('pit', 5, 45.8)]
students = np.array(student_detail, dtype=data_type)
print('original array: ')
print(student_detail)
print('sorted by height: ')
print(np.sort(students, order = 'name'))