''' module of functions used in class.
'''

def is_nucl_str_clean(nucl_str: str) -> dict:
    ''' Returns a dictionary of index/values pairs
        in nucleotide string where bad values exist.
        Returns empty dictionary if nucleotide string
        is clean
    '''
    # garbage filter: ensure input is a string
    assert isinstance(nucl_str, str),\
        "input must be a string."
    # initialization
    bad_values = {}
    # implementation of the algorithm
    for item in enumerate(nucl_str):
        if item[1] not in 'acgtACGT':
            bad_values[item[0]] = item[1]
    return bad_values
    
def per_gc_content(nucl_str: str) -> float:
    ''' Given a clean nucleotide string as input,
        returns the percent GC content in the string.
        >>>per_gc_content('gattacaga')
        33.333333333333336
        >>>per_gc_content('GATTACA')
        28.571428571428573
    '''
    # make sure input is clean nucleotide string
    assert isinstance(nucl_str, str),\
        "input must be a clean nucleotide string."
    bad_values = is_nucl_str_clean(nucl_str)
    assert not bad_values,\
        (f"input has non-nucleotides at these index positions:\n"
         f"\t{bad_values}")
    # initialization
    nucl_str = nucl_str.upper()
    # implementation of algorithm
    return 100 * (nucl_str.count('G') + nucl_str.count('C'))\
               / len(nucl_str)

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
