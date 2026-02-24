''' is_nucl_str_clean development file
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
