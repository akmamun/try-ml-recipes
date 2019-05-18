# for loop 
for i in range(4, 11):
  print(i)

array =[1,3,5]
for i in range( len(array)):
  print(i, array[i])

# instead of range
array =[1,3,5]
for i, val in enumerate(array):
    print(i, val)

#multipe list iterate
array =[1,3,5]
s = [2,5,7]
for i, val in zip(array, s):
    print(i, val)

# find values up to 10 for which x % 2 is zero
is_even = lambda x: x % 2 == 0
for val in filter(is_even, range(10)):
    print(val, end=' ')

import pandas as pd
df = pd.DataFrame({'label': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'value': [1, 2, 3, 4, 5, 6]})
df

import numpy as np
from scipy import interpolate

# choose eight points between 0 and 10
x = np.linspace(0, 10, 8)
y = np.sin(x)

# create a cubic interpolation function
func = interpolate.interp1d(x, y, kind='cubic')

# interpolate on a grid of 1,000 points
x_interp = np.linspace(0, 10, 1000)
y_interp = func(x_interp)

# plot the results
plt.figure()  # new figure
plt.plot(x, y, 'o')
plt.plot(x_interp, y_interp);
