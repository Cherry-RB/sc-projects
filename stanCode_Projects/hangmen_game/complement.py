"""
File: complement.py
Name:Cherry
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    considering all words of dna and its complement
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    complement = build_complement(dna)
    print('The complement of '+dna+' is '+complement)


def build_complement(dna):
    complement = ''
    dna = dna.upper()
    for i in range(len(dna)):
        if dna[i] == 'A':
            complement += 'T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'G':
            complement += 'C'
        elif dna[i] == 'C':
            complement += 'G'
    return complement


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
