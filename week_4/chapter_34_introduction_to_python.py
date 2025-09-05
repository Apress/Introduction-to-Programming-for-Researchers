with open('datafile/reformatted_Unigene.fa') as inFile:
    # in the next line, we chain methods
    LoS = inFile.read().splitlines()
    # the first method, .read(), reads the contents
    # of the file into session memory as a single string.
    # the second method, .splitlines(),
    # is a string method that splits the string along
    # newline characters (\n), and puts the lines
    # into a list while preserving their order.
    # as a result, the file contents are held in memory
    # in their original order as a list-of-strings, or LoS.

