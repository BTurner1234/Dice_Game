import numpy as np

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

def calculate_probabilities(dice_values):
    """
    This function calculates the probabilities for a given set of dice values.

    Args:
        dice_values: A list of dice face values.

    Returns:
        A list of probabilities for each dice value.
    """
    dice_values.sort(reverse=True)
    max_value = dice_values[0]

    # Initialise array to store the number of dice at or above each value
    count_array = [0] * max_value
    for value in dice_values:
        count_array[value - 1] += 1

    # Reverse and cumulative sum
    count_array.reverse()
    cumulative_count = np.cumsum(count_array)

    # Initialise probabilities array
    probabilities = [0] * max_value

    for i in range(max_value):
        values_coefficient = 1 / mult_sum(dice_values[:cumulative_count[i]])
        total_sum = sum(
            np.power(max_value - i, j) * np.power(max_value - i - 1, cumulative_count[i] - 1 - j)
            for j in range(cumulative_count[i])
        )
        probabilities[i] = values_coefficient * total_sum

    probabilities.reverse()
    return probabilities

def calculate_winning_probabilities(probs_1, probs_2):
    """
    This function calculates the probabilities of winning for both players and the probability of a tie.

    Args:
        probs_1: Probabilities for player 1.
        probs_2: Probabilities for player 2.

    Returns:
        A tuple with the probabilities of player 1 winning, player 2 winning, and a tie.
    """
    cumsum_1 = np.cumsum(probs_1)
    cumsum_2 = np.cumsum(probs_2)

    # Ensure both cumulative sums have the same length
    max_length = max(len(cumsum_1), len(cumsum_2))
    cumsum_1 = np.pad(cumsum_1, (0, max_length - len(cumsum_1)), constant_values=1)
    cumsum_2 = np.pad(cumsum_2, (0, max_length - len(cumsum_2)), constant_values=1)

    prob_2_wins = sum(cumsum_1[i-1] * probs_2[i] for i in range(1, len(probs_2)))
    prob_tie = sum(probs_1[i] * probs_2[i] for i in range(min(len(probs_1), len(probs_2))))
    prob_1_wins = sum(cumsum_2[i-1] * probs_1[i] for i in range(1, len(probs_1)))

    return prob_1_wins, prob_2_wins, prob_tie

