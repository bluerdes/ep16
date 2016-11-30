"""Provide functions which compute the expected utility value and
certainty equivalent of a lottery under prospect theory utility.

"""


def v_prospect_theory(lottery, preferences):
    """Return the expected utility value of a gamble described in the
    dictionary *lottery* under prospect theory utility with preference
    parameters in the dictionary *preferences*.

    """

    v = 0.0
    for outcome in lottery:
        v += lottery[outcome] * u_prospect_theory(outcome, preferences)

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


def ce_prospect_theory(lottery, preferences):
    """Return the certainty equivalent of a gamble described in dictionary
    *lottery* under prospect theory utility with preference parameters
    in the dictionary *preferences*.

    """

    return
