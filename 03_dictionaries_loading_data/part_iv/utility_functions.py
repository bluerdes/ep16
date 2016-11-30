"""Provide functions which compute the expected utility value
and certainty equivalent of a lottery under prospect theory
or exponential utility.

"""

from math import exp, log


def v(lottery, u, preferences):
    """Return the expected utility value of a gamble described in the
    dictionary *lottery* under the utility function *u* with preference
    parameters in the dictionary *preferences*.

    """

    v = 0.0
    for outcome in lottery:
        v += lottery[outcome] * u(outcome, preferences)

    return v


def u_prospect_theory(z, preferences):
    """Return the utility evaluation of a monetary quantity *z* under
    prospect theory preferences with utility curvature parameter
    *preferences['gamma']* and loss aversion parameter
    *preferences['lambda']*.

    """

    if z >= 0:
        u = z ** (1 - preferences['gamma'])
    elif z < 0:
        if preferences['gamma'] <= 0:
            u = -preferences['lambda'] * (-z) ** (1 + preferences['gamma'])
        elif preferences['gamma'] > 0:
            u = -preferences['lambda'] * (-z) ** (1 - preferences['gamma'])
    return u


def u_prospect_theory_inverse(x, preferences):
    """Return the inverse of a prospect theory utility function
    for value *x* with utility curvature parameter
    *preferences['gamma']* and loss aversion parameter
    *preferences['lambda']*.

    """

    return


def u_exponential(z, preferences):
    """Return the utility evaluation of a monetary quantity *z* under
    exponential utility with utility curvature parameter
    *preferences['gamma']* and loss aversion parameter
    *preferences['lambda']*.

    """

    return


def u_exponential_inverse(x, preferences):
    """Return the inverse of an exponential utility function
    for value *x* with utility curvature parameter
    *preferences['gamma']* and loss aversion parameter
    *preferences['lambda']*.

    """

    return


def ce(lottery, preferences):
    """Return the certainty equivalent of a gamble described in dictionary
    *lottery* under the utility function described in the dictionary
    *preferences*.

    """

    # Select the correct utility function based on input
    if preferences['function'] == 'prospect theory':
        u = u_prospect_theory
        u_inverse = u_prospect_theory_inverse
    elif preferences['function'] == 'exponential':
        u = u_exponential
        u_inverse = u_exponential_inverse
    else:
        raise ValueError('Unknown utility function: ' + preferences['function'])

    # Return the certainty equivalent
    return
