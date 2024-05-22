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
player_1 = [5, 6, 3, 1, 6]
player_2 = [3, 8, 1, 2]

player_1.sort()
player_2.sort()

player_1.reverse()
player_2.reverse()

player_1_num_dice_with_value = [0] * player_1[0]
player_2_num_dice_with_value = [0] * player_2[0]
count = 0
for i in player_1:
    count += 1
    player_1_num_dice_with_value[i-1] += 1

player_1_num_dice_with_value.reverse()
player_1_num_dice_with_value = np.cumsum(player_1_num_dice_with_value)

count = 0
for i in player_2:
    count += 1
    player_2_num_dice_with_value[i-1] += 1

player_2_num_dice_with_value.reverse()
player_2_num_dice_with_value = np.cumsum(player_2_num_dice_with_value)

print(player_1)
print(player_1_num_dice_with_value)

probs_1 = [0]*player_1[0]

for i in range(0, player_1[0]):
    probs_1[i] = 1/mult_sum(player_1[0:player_1_num_dice_with_value[i]])
    total = 0
    for j in range(player_1_num_dice_with_value[i]):
        total +=1

print(probs_1)
