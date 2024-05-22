import numpy as np
import math

def mult_sum(num_list):
  """
  This function calculates the product of all elements in a list.

  Args:
      num_list: A list of numbers.

  Returns:
      The product of all elements in the list.
  """
  product = 1
  for num in num_list:
    product *= num
  return product

# Testing example 
k_1 = [5, 6, 3, 1, 6]
k_2 = [3, 8, 1, 2]

k_1.sort()
k_2.sort()

k_1.reverse()
k_2.reverse()

n_1 = [0] * k_1[0]
n_2 = [0] * k_2[0]
count = 0
for i in k_1:
    count += 1
    n_1[i-1] += 1

n_1.reverse()
n_1 = np.cumsum(n_1)

count = 0
for i in k_2:
    count += 1
    n_2[i-1] += 1

n_2.reverse()
n_2 = np.cumsum(n_2)

print(k_1)
print(n_1)

probs_1 = [0]*k_1[0]

for i in range(0, k_1[0]):
    probs_1[i] = 1/mult_sum(k_1[0:n_1[i]])
    total = 0
    for j in range(n_1[i]):
        total += np.power((k_1[0]-i),j) * np.power((k_1[0]-i-1), n_1[i]-1-j)
        #np.power(4,3)
        #print(j)
        #print(n_1[i]-1-j)
    probs_1[i] *= total
