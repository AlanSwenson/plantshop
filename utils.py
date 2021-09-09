import math
from textwrap import wrap


def check_length(n):
    if n > 0:
        digits = int(math.log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n)) + 2
    return digits


def split_dna(dna):
    dna_chunks = wrap(str(dna), 2)
    return dna_chunks


def create_attribute(name, dna_slice):
    att = {
        "trait_type": name,
        "value": dna_slice,  # using the dictionary found in collection_func get the appropriate strings
    }
    return att
