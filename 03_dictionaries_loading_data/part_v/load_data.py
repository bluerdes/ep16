"""Load the data provided with the exercise."""


def load_lotteries():
    """Read the contents of the file lotteries.txt in the input directory
    and return a list with dictionaries of the different lotteries.

    """

    # Define list of lotteries to be returned.
    lotteries_out = []
    with open('../input/lotteries.txt') as in_file:
        for line in in_file:
            if not line.startswith('prob_low'):
                # Lottery characteristics as a list of strings.
                lottery_raw = line.split('\t')
                prob_low = float(lottery_raw[0])
                # Convert to dictionary as required.
                lottery_dict = {
                    float(lottery_raw[1]): prob_low,
                    float(lottery_raw[2]): 1 - prob_low
                }
                # Append to list of lotteries to be returned.
                lotteries_out.append(lottery_dict)

    return lotteries_out
