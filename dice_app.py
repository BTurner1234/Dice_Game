import streamlit as st
import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from calculations import calculate_probabilities, calculate_dice_game_probabilities

# Add a title for the whole app
st.title("Dice Game Probability Calculator")

# Add an explanation under the title
st.markdown("""
    ### Welcome to the Dice Game Probability Calculator!

    In this app, you can simulate a game involving two players rolling dice, and we can calculate the probabilities of each player winning, along with the chances of a tie.

    **How the game works:**
    
    - Each player selects the number of dice they will roll and specifies the size (number of sides) for each die.
    - The player's score is determined by the highest value rolled among all their dice.
    - For example, if Player 1 selects 3 dice with sizes 4, 6, and 7, they will roll a 4-sided die, a 6-sided die, and a 7-sided die. If their rolls are 3, 2, and 6, their score would be 6.
    - This app calculates the probability of each player rolling the highest score based on the number and size of the dice.
    - The results are displayed graphically, along with the overall winning probabilities for Player 1, Player 2, and a tie.

    Adjust the number and size of the dice in the sidebar to see how the probabilities change. 
    This simulation helps you understand how the size of dice and the number of dice impact the outcome.

    Good luck!
""")

# Set up the side panel for player options
st.sidebar.title("Player Options")

# Section for Player 1 options
with st.sidebar.expander("Player 1 Options"):
    num_dice_p1 = st.slider("Number of Dice (Player 1)", min_value=1, max_value=10, value=3)
    dice_sizes_p1 = []
    for i in range(num_dice_p1):
        size = st.number_input(f"Die {i+1} Size (Player 1)", min_value=1, max_value=20, value=6, key=f"p1_die{i+1}")
        dice_sizes_p1.append(size)

# Section for Player 2 options
with st.sidebar.expander("Player 2 Options"):
    num_dice_p2 = st.slider("Number of Dice (Player 2)", min_value=1, max_value=10, value=3)
    dice_sizes_p2 = []
    for i in range(num_dice_p2):
        size = st.number_input(f"Die {i+1} Size (Player 2)", min_value=1, max_value=20, value=6, key=f"p2_die{i+1}")
        dice_sizes_p2.append(size)

try:
    prob_1_wins, prob_2_wins, prob_tie = calculate_dice_game_probabilities(dice_sizes_p1, dice_sizes_p2)

    # Display results with larger text size in the colored boxes
    st.markdown(f"""
        <div style="display: flex; justify-content: space-around; margin-bottom: 20px;">
            <div style="background-color: #007bff; border-radius: 10px; padding: 10px; width: 30%; text-align: center;">
                <h4 style="color: white;">Player 1 Wins</h4>
                <p style="color: white; font-size: 24px;">{100 * prob_1_wins:.1f}%</p>
            </div>
            <div style="background-color: #28a745; border-radius: 10px; padding: 10px; width: 30%; text-align: center;">
                <h4 style="color: white;">Tie</h4>
                <p style="color: white; font-size: 24px;">{100 * prob_tie:.1f}%</p>
            </div>
            <div style="background-color: #dc3545; border-radius: 10px; padding: 10px; width: 30%; text-align: center;">
                <h4 style="color: white;">Player 2 Wins</h4>
                <p style="color: white; font-size: 24px;">{100 * prob_2_wins:.1f}%</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Calculate probabilities for both players
    probs_p1 = calculate_probabilities(dice_sizes_p1)
    probs_p2 = calculate_probabilities(dice_sizes_p2)

    # Ensure both probability arrays are the same length by padding with zeros
    max_dice_value = max(len(probs_p1), len(probs_p2))
    probs_p1 += [0] * (max_dice_value - len(probs_p1))  # Pad Player 1's probabilities
    probs_p2 += [0] * (max_dice_value - len(probs_p2))  # Pad Player 2's probabilities

    # Create overlapping histograms with transparency
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(1, max_dice_value + 1)

    ax.bar(x, probs_p1, color='blue', alpha=0.6, label='Player 1')  # Blue bars for Player 1
    ax.bar(x, probs_p2, color='red', alpha=0.6, label='Player 2')   # Red bars for Player 2

    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Probability")
    ax.set_title("Probability of Highest Roll")
    ax.legend()

    st.pyplot(fig)

    # Add mathematical explanation
    st.markdown("""
    ## Mathematical Explanation

    We will begin by using an example as motivation. We will calculate the probability of each value being the highest score out of a group of dice, do this for both players, and then compare between the two to find the probability of each player winning, along with a tie.

    **Example:**

    Let's assume player 1 has four dice, with sides 9, 7, 7, and 5.
    
    - The probability of 9 being the highest score is simply $$\\frac{1}{9}$$, as it must come from the 9-sided die.
    
    - The same is true for 8 being the highest score, the probability is equal to $$\\frac{1}{9}$$.

    **Calculating for 7:**
    
    For 7, we will work out the probability of all dice at or above 7 scoring this value, while avoiding overlapping probabilities.
    
    - First, we calculate the probability of the first die scoring 7, including all other dice scores at or below that value.
    - Then, we calculate the probability for each successive die to score 7, **excluding** the previous die from scoring 7 (i.e., they must score below), to cancel out overlapping probabilities.

    Since three dice can score 7, we get three probabilities:
    """)

    # Using LaTeX for the calculation:
    st.latex(r'''
    \left( \frac{1}{9} \right), \quad \left( \frac{6}{9} \cdot \frac{1}{7} \right), \quad \left( \frac{6}{9} \cdot \frac{6}{7} \cdot \frac{1}{7} \right)
    ''')

    # Continuing the markdown
    st.markdown("""
        Which we will add together to find the total probability.
        
        This can be rewritten as:
    """)

    # Using LaTeX again for the formula:
    st.latex(r'''
    \left( \frac{1}{9} \cdot \frac{7}{7} \cdot \frac{7}{7} \right) + \left( \frac{6}{9} \cdot \frac{1}{7} \cdot \frac{7}{7} \right) + \left( \frac{6}{9} \cdot \frac{6}{7} \cdot \frac{1}{7} \right)
        = \frac{1}{9 \cdot 7 \cdot 7} \cdot \left( 7^2 + \left( 6 \cdot 7 \right) + 6^2 \right)
    ''')

    # Generalization formula in LaTeX
    st.markdown("""
        **Generalisation:**

        We can now generalise for all values from 1 to the maximum value of the largest die of player 1. The probability is given by:
    """)

    st.latex(r'''
    P_1(k) = \frac{1}{\prod_{i=k} v_{k+}} \cdot \sum_{i=0}^{n-1} \left( k^i \cdot (k-1)^{n-1-i} \right)
    ''')

    st.markdown(r'''
    Where:
    - $$P_1(k)$$ is the probability of player 1 having a score of $$k$$.
    - $$k$$ is the value being considered.
    - $$n$$ is the number of dice with a maximum value at, or above, $$k$$.
    - $$V_{k+}$$ are the maximum values of these dice. (At or above $$k$$).

    This gives a probability distribution for the highest value across the dice.

    This gives us the histogram for each player we see in the graphic above, which can then be used to calculate the winning and tieing probabilities.
    
    ---

    **Probability for Player 1 Winning:**

    To find the probability for Player 1 winning, we take the sum from $$1$$ to $$k_{max}$$ as follows:

    ''')

    st.latex(r'''
    P(\text{Player 1 win}) = \sum_{i=1}^{k_{\text{max}}} \left[ P_1(i) \cdot \left( \sum_{j=1}^{i-1} P_2(j) \right) \right]
    ''')

    st.markdown(r'''
    Where:
    - $$P_1(i)$$ is the probability that Player 1 rolls $$i$$.
    - $$P_2(j)$$ is the probability that Player 2 rolls $$j$$ with $$j < i$$.
    - $$max$$ represents the maximum value on the largest die.

    **Probability of a Tie:**

    The probability of a tie can be found as:
    ''')

    st.latex(r'''
    P(\text{tie}) = \sum_{i=1}^{k_{\text{max}}} \left[ P_1(i) \cdot P_2(i) \right]
    ''')

    st.markdown(r'''
    Where:
    - $$P_1(i)$$ is the probability that Player 1 rolls $$i$$.
    - $$P_2(j)$$ is the probability that Player 2 rolls $$j$$.
    - $$max$$ represents the maximum value on the largest die.
    ''')

    st.markdown(r'''
    **Probability for Player 2 Winning:**
    ''')

    st.latex(r'''
    P(Player \space 2 \space win) = 1 - P(tie) - P(Player \space 1 \space win)
    ''')

    st.markdown(r'''
    ---
    ''')

    st.markdown("## Probability Calculations Code")

    # Open the local 'calculations.py' file
    with open("calculations.py", "r") as f:
        code = f.read()

    # Display the code
    st.code(code, language='python')

    # Add the section at the bottom for project reference
    st.markdown("""
    This interactive app is part of a project, extended from this blog post: [Raindrops & A Game Of Dice](https://mathsmusings.hashnode.dev/raindrops-a-game-of-dice)
    """)

    st.markdown("""
    ---
    <div style="text-align: right;">
        Created by <a href="https://www.linkedin.com/in/bailey-t-7b7047313/">Bailey Turner</a>
    </div>
    """, unsafe_allow_html=True)

except ValueError as e:
    st.error(f"Error: {str(e)}")
