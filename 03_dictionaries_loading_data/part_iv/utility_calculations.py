"""Compute the certainty equivalent of a lottery defined here.

"""

from utility_functions import ce


# Define the characteristics of the individuals.
preference_specifications = [
    {'function': 'prospect theory', 'gamma': 0.8, 'lambda': 1.0},
    {'function': 'exponential', 'gamma': 0.00009, 'lambda': 1.0}
]

# Define the characteristics of the lottery.
lottery = {-500.0: 0.4, 700.0: 0.6}

# Define a basis string for the output.
out = 'Certainty equivalent for gamma={:6.4f} and lambda={:.1f} under {} utility: {:6.2f}\n'

with open('../output/utility_calculations_part_iv.txt', 'w') as out_file:
    for p in preference_specifications:
        # Calculate the certainty equivalent.

        # Write the parameters and certainty equivalent to the file.

        # Delete this -- placeholder so that Spyder doesn't show an error.
        pass
