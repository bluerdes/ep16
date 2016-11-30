"""Compute the certainty equivalent of a lottery under prospect theory
utility and various preference parameter combinations.

"""

from utility_functions import ce_prospect_theory


# Define the characteristics of the lottery.
lottery = {-500.0: 0.4, 700.0: 0.6}

# Define a basis string for the output.
out = 'Certainty equivalent for gamma={: .2f} and lambda={:.1f}: {:6.2f}'

# Calculate the utility values
for utility_curvature in (-0.8, 0.0, 0.8):
    for loss_aversion in (1.0, 2.5):
        # Define the preference dictionary.
        preferences = {'gamma': utility_curvature, 'lambda': loss_aversion}
        # Calculate the certainty equivalent.

        # Print the certainty equivalent to the screen.
        print(out.format())
