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
    trait = ""
    # 1st gene is genus
    if name == "genus":
        if int(dna_slice) % 10 == 1:
            trait = "monstera"
        else:
            trait = "common house plant"
    # 3rd gene is color
    elif name == "color":
        if int(dna_slice) % 100 == 1:
            trait = "gold"
        else:
            trait = "typical"
    # catchall for unimplemented genes
    else:
        trait = "undiscovered"
    return format_trait(name, trait)


def format_trait(name, trait):
    attribute = {
        "trait_type": name,
        "value": trait,  # using the dictionary found in collection_func get the appropriate strings
    }
    return attribute
