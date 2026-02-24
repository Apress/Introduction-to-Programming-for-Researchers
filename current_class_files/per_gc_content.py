''' development file of per_gc_content function
'''

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
    # initialization
    nucl_str = nucl_str.upper()
    # implementation of algorithm
    return 100 * (nucl_str.count('G') + nucl_str.count('C'))\
               / len(nucl_str)
