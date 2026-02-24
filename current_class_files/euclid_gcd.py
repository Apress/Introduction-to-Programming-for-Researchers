''' development file for euclid_gcd function
'''

def euclid_gcd(nat_a: int, nat_b: int) -> int:
    ''' Returns the greatest common divisor
        of nat_a and nat_b
        >>>euclid_gcd(53667, 25527)
        201
    '''
    # garbage filter: input is expected input
    # two natural numbers
    assert (isinstance(nat_a, int) and nat_a > 0)\
       and (isinstance(nat_b, int) and nat_b > 0),\
       "nat_a and nat_b must be natural numbers."
    # implementation of the algorithm
    while nat_b:
        nat_a, nat_b = nat_b, nat_a % nat_b
    return nat_a
