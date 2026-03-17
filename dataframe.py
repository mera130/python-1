import pandas as pn
import numpy as np
exam_data = {'name': ['anatasia', 'lara', 'adriana', 'katherine', 'jones', 'harry'],
             'scores': [16.9, 9, 12, 5, 20, np.nan],
             'attempts': [1,2,3,1,2,1],
             'qualify': ['yes', 'no', 'yes', 'no', 'yes', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f']
df = pn.DataFrame(exam_data, index = labels)
print('info about this data')
print(df.info())
print(df.head(6))
