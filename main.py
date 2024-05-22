from Dice_Game import calculate_probabilities, calculate_winning_probabilities

# Testing example
k_1 = [8, 8, 3, 8, 5, 8]  # Player 1's dice (list of face values)
k_2 = [9, 7, 6, 4]  # Player 2's dice (list of face values)

probs_1 = calculate_probabilities(k_1)
probs_2 = calculate_probabilities(k_2)

prob_1_wins, prob_2_wins, prob_tie = calculate_winning_probabilities(probs_1, probs_2)

# Ensure total probability = 1
total_prob = prob_1_wins + prob_2_wins + prob_tie

# Print results
print(f"Probability player 1 wins: {prob_1_wins * 100:.1f}%")
print(f"Probability player 2 wins: {prob_2_wins * 100:.1f}%")
print(f"Probability of a tie: {prob_tie * 100:.1f}%")
