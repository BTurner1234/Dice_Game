import numpy as np

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

for i in range(0, player_1[0]):
    for j in range(0, i):
        pass